function list_common(value_set){
    const table_row = document.createElement('tr')
    for (const [key, value] of Object.entries(value_set)){
        const table_data = document.createElement('td')
        if (Array.isArray(value)){
            for (val of value){
                const value_span = document.createElement('span');
                value_span.innerHTML = val
                table_data.append(value_span)
            }
        }else if(typeof value === "boolean"){
            const value_span = document.createElement('span');
            if(value){
                value_span.className = 'win';
            }else{
                value_span.className = 'lose';
            }
            table_data.append(value_span)
        }else{
            table_data.innerHTML = value;  
        }
              
        table_row.append(table_data)       
    }
    return table_row;
}
function display_current_num_set(current_num_set, common_val_dic){
    var compare_val_div = document.querySelector('#compare_val_div');    
    let num_of_common_heading = '';

    for (const [common_list, common_list_values] of Object.entries(common_val_dic)){
        if (common_list_values.length !== 0){
            const data_table = document.createElement('table');
            data_table.className = 'dataset_table';
            data_table.innerHTML = `
                <tr>
                    <th>Compared Date</th>
                    <th>Compared Num Set</th>
                    <th>Win</th>
                    <th>Num of Common</th>
                    <th>Common Num Set</th>                    
                </tr>
            `;
            for (value of common_list_values){     
                let table_row = list_common(value)               
                data_table.append(table_row)
            }
            
            switch(true){
                case common_list.includes('five'):
                    num_of_common_heading = '5';
                    break;
                case common_list.includes('four'):
                    num_of_common_heading = '4';
                    break;
                case common_list.includes('three'):
                    num_of_common_heading = '3';
                    break;
                case common_list.includes('two'):
                    num_of_common_heading = '2';
                    break;
                case common_list.includes('one'):
                    num_of_common_heading = '1';
                    break;
                default:
                    num_of_common_heading = '0';
                    break;
            }

            const heading = document.createElement('h3');
            heading.innerHTML = `${num_of_common_heading} Number of Common Values - ${common_list_values.length} time(s)`;

            compare_val_div.append(heading)
            compare_val_div.append(data_table)
        }        
    }
}