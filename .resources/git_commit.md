# HowTo: convenio de commits de git

Documento interno. Resumen de buenas prácticas para escribir commits, 
pensado para que el historial sea legible y útil a futuro (changelog, 
`git log`, `git blame`, bisect).

## La regla de oro

Un commit = un cambio completo y coherente. Si no puedes describirlo en
una línea, o mezclas refactor con funcionalidad y tests, divídelo en
varios commits.

## Formato del mensaje

```
<tipo>: <resumen en minúsculas, imperativo>

<cuerpo opcional: el porqué, no el qué>
```

- **Asunto**: máx. 50 caracteres, imperativo y en minúsculas. Sin punto
  final. Imperativo significa que completa la frase "si se aplica, este
  commit *añade* el comando split", no "añadiendo" ni "añadido".
- **Cuerpo**: separado del asunto por una línea en blanco. Opcional,
  pero útil cuando la decisión no es obvia (por qué se eligió un
  enfoque, qué bug provocaba, enlaces a issues). Máx. 72 columnas.
- **Idioma**: español, como el resto del proyecto.

## Tipos permitidos (Conventional Commits simplificado)

| Tipo       | Uso                                                              |
| ---------- | ---------------------------------------------------------------- |
| `feat`     | Funcionalidad nueva visible al usuario (comando, opción, locale) |
| `fix`      | Corrección de un bug existente                                   |
| `refactor` | Cambio interno sin alterar el comportamiento                     |
| `docs`     | Documentación (README, man page, docstrings, changelog)          |
| `test`     | Añadir o corregir tests, fixtures                                |
| `build`    | Empaquetado, PyInstaller, uv, dependencias                       |
| `chore`    | Tareas de mantenimiento (pre-commit, scripts, renombres)         |

Si un commit toca varios tipos, el del mayor impacto gana; si no hay
mayoría clara, es señal de que debe partirse.

## Ejemplos

Bien:

```
feat: añade comando split con marcas de tiempo
fix: corrige conflicto de salida en encode en masa con SKIP
refactor: extrae filtros comunes a FiltersMixin
test: añade suite E2E del binario PyInstaller
```

## Flujo de trabajo

```bash
# Antes de comitear
git status
git diff
# Trocear si el cambio es grande
git add -p
# Comitea con el mensaje completo (multi-línea)
git commit
# Revisa antes de hacer push, si se debe corregir, enmienda
git commit --amend
# Para commits en WIP, trabajar en ramas o con fixup
git commit --fixup=<sha>
git rebase -i --autosquash <sha>
```

## Checklist rápido antes de `git push`

- [ ] ¿Cada commit compila y pasa los tests por sí solo?
- [ ] ¿El asunto describe el cambio sin ver el diff?
- [ ] ¿El tipo corresponde realmente al contenido?
- [ ] ¿Nada de ficheros temporales, secretos dentro?
