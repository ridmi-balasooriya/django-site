from django.shortcuts import render, redirect
from .models import DataSet
from .forms import AddDataForm
from django.http import JsonResponse


def get_data_dic(current_id=""):

    data_dic = []

    if (current_id):
        dataset = DataSet.objects.all().exclude(id=current_id)
    else:
        dataset = DataSet.objects.all()

    # make number set to truple and create data list
    for data in dataset:
        temp_dic = {}
        temp_dic['date'] = data.date
        temp_dic['num_set'] = (data.num_one, data.num_two,
                               data.num_three, data.num_four, data.num_five)
        temp_dic['win'] = data.win
        data_dic.append(temp_dic)

    return data_dic


def compare_set(temp_numset, next_data):
    sorted_with_dic = {}

    common_val = set(temp_numset) & set(next_data['num_set'])
    sorted_with_dic['compared_date'] = next_data['date']
    sorted_with_dic['compared_dataset'] = next_data['num_set']
    sorted_with_dic['compare_win'] = next_data['win']
    sorted_with_dic['num_of_common_nums'] = len(common_val)
    sorted_with_dic['common_nums'] = sorted(list(common_val))

    return sorted_with_dic


def check_common(x, y):
    return x['num_of_common_nums'] == y


def get_common_list(num_of_common_num, data_dic):

    common_list = []

    for data in data_dic:

        if 'sorted_with' in data:
            common = list(
                filter(lambda d: check_common(d, num_of_common_num), data['sorted_with']))

            for c in common:
                temp_data = {}

                temp_data['date'] = data['date']
                temp_data['num_set'] = data['num_set']
                temp_data['win'] = data['win']
                temp_data['sorted_with'] = c
                common_list.append(temp_data)
        else:
            common = ''
            common = check_common(data, num_of_common_num)
            if common:
                common_list.append(data)

    return common_list


def get_common_val_set(data_dic, current_num_set):
    compared_dic = []
    common_val_dic = {}

    for data in data_dic:
        sorted_with_dic = compare_set(current_num_set, data)
        compared_dic.append(sorted_with_dic)

    common_five_list = get_common_list(5, compared_dic)
    common_four_list = get_common_list(4, compared_dic)
    common_three_list = get_common_list(3, compared_dic)
    common_two_list = get_common_list(2, compared_dic)
    common_one_list = get_common_list(1, compared_dic)

    common_val_dic['common_five_list'] = common_five_list
    common_val_dic['common_four_list'] = common_four_list
    common_val_dic['common_three_list'] = common_three_list
    common_val_dic['common_two_list'] = common_two_list
    common_val_dic['common_one_list'] = common_one_list

    response_data = {'current_num_set': current_num_set,
                     'common_val_dic':  common_val_dic}

    return response_data


def data_home(request):
    dataset = DataSet.objects.all()
    return render(request, 'data_home.html', {'dataset': dataset})


def analyse_data(request):

    common_five_list = []
    common_four_list = []
    common_three_list = []
    common_two_list = []
    common_one_list = []
    common_val_dic = {}

    data_dic = get_data_dic()

    for i, data in enumerate(data_dic):
        temp_pos = i+1
        temp_numset = data['num_set']

        # update the data_dic with compared data list of dictionaries.
        update_dic = data_dic[i]
        update_dic['sorted_with'] = []

        for next_data in data_dic[temp_pos:]:
            if (temp_pos <= len(data_dic) - 1):
                sorted_with_dic = compare_set(temp_numset, next_data)
                update_dic['sorted_with'].append(sorted_with_dic)
                temp_pos += 1

    common_five_list = get_common_list(5, data_dic)
    common_four_list = get_common_list(4, data_dic)
    common_three_list = get_common_list(3, data_dic)
    common_two_list = get_common_list(2, data_dic)
    common_one_list = get_common_list(1, data_dic)

    common_val_dic['common_five_list'] = common_five_list
    common_val_dic['common_four_list'] = common_four_list
    common_val_dic['common_three_list'] = common_three_list
    common_val_dic['common_two_list'] = common_two_list
    common_val_dic['common_one_list'] = common_one_list

    return render(request, 'analyse_data.html', {'common_val_dic': common_val_dic})


def check_posibility(request):
    return render(request, 'check_posibility.html')


def add_new_data(request):
    form = AddDataForm()

    if request.method == 'POST':
        filled_form = AddDataForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('/data_analyse')

        else:
            note = 'Invalide Details.'
            return render(request, 'add_new_data.html', {'add_data_form': form, 'erro_note': note})
    else:
        return render(request, 'add_new_data.html', {'add_data_form': form})


def individual_posibility(request, data_id):
    data = DataSet.objects.get(id=data_id)
    individual_date = data.date

    current_num_set = (int(data.num_one), int(data.num_two), int(
        data.num_three), int(data.num_four), int(data.num_five))

    data_dic = get_data_dic(data_id)

    response_data = get_common_val_set(data_dic, current_num_set)

    return render(request, 'individual_posibility.html', {'response_data': response_data, 'individual_date': individual_date})


def ajax_view(requset):

    if requset.method == 'POST':
        num_one = requset.POST.get('num_one')
        num_two = requset.POST.get('num_two')
        num_three = requset.POST.get('num_three')
        num_four = requset.POST.get('num_four')
        num_five = requset.POST.get('num_five')

        current_num_set = (int(num_one), int(num_two), int(
            num_three), int(num_four), int(num_five))

        data_dic = get_data_dic()

        response_data = get_common_val_set(data_dic, current_num_set)

        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalide Method'})
