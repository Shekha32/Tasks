
Вам на ревью пришла функция для извлечения уникальных имен датасетов
из списка mongo-коллекций. Перечислите проблемы, которые вы видите в коде,
и напишите реализацию функции после рефакторинга.

def extr_Names(collections_list, datasets=[]):
        """
        Extract unicue dataset names from collections list.
        Colletions have format dataset_name@dataset_id
        """
        if len(collections_list) > 0:
                for c in collections:
                        index=c.index('@')
                        if index > 0:
                                name=c[:index]
                        datasets.append(name)
        else:
                return datasets

        dataset_names=[]
        for i in range(0, len(datasets)):
                d=datasets[i]
                if d[0] != '_' and d[1] != '_':
                        if d not in dataset_names:
                                dataset_names.append(d)
                else:
                        print('Skip' + d)
        return dataset_names.sort()
