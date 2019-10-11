from EnWiktCJK import ZhDataDialSynIndexCrawler


if __name__ == '__main__':
    """
    simple test
    """
    crawler = ZhDataDialSynIndexCrawler()

    params = {'title': 'Special:PrefixIndex',
              'prefix': 'Module:zh/data/dial-syn',
              'namespace': 0,'stripprefix': 1}

    dialsyn_datamodules = crawler.extract_all_indices(params)
    for i, dialsyn in enumerate(dialsyn_datamodules):
        print(i+1, dialsyn)







