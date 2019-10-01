def arbol(directorio):
    print(f'+ {directorio}')
    for archivo in sorted(directorio.rglob('*')):
        profundidad = len(archivo.relative_to(directorio).parts)
        espacio = '    ' * profundidad
        print(f'{espacio}+ {archivo.name}')