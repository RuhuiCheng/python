import os, csv
import hashlib

input_path = '/home/crh/temp2018/local/mac_addr_data/output'
output_path = '/home/crh/temp2018/local/mac_addr_data/output-md5'
headers = ['mac','mac_company','mac_time','mac_lat','mac_lon','geo_hash5','geo_hash6','geo_hash7','geo_hash8','geo_hash9','geo_category','client_id']

class csv_md5():
    
    def run(self):
        for maindir, subdir, file_name_list in os.walk(input_path):
            for filename in file_name_list:
                input_file = os.path.join(maindir, filename)
                dt = self.file_read(input_file)
                output_dir = maindir.replace('output','output-md5')
                if (os.path.exists(output_dir) == False):
                    os.makedirs(output_dir)
                output_file = os.path.join(output_dir,filename)
                self.file_write(output_file,dt)

    def file_read(self, input_file):
        ls =[]
        with open(input_file) as fr:
            reader = csv.DictReader(fr)
            for row in reader:
                data = row['mac']
                data = data.replace(':','')
                hash = hashlib.md5(data.encode('utf-8'))
                row['mac'] = hash.hexdigest()
                ls.append(row)
        return ls

    def file_write(self, output_file,datas):
        with open(output_file,'w',newline='') as fw:
            writer = csv.DictWriter(fw,headers)
            writer.writeheader()
            writer.writerows(datas)

if __name__ == "__main__":
    obj = csv_md5()
    obj.run()
