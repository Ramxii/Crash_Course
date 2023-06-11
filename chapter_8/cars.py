def build_a_car(manufacturer, model_name, **car_info):
    """Creates a dictionary containing vehicle information"""
    car_info['brand'] = manufacturer
    car_info['model'] = model_name
    return car_info

car_build = build_a_car('Bmw', 'x1', driver='left', tires='off-road')

print(car_build)

