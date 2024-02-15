const fs = require('fs');
const {Parser} = require("acorn")

const sourceType = process.argv[2]

const src = fs.readFileSync(process.argv[3], 'utf8')
const tree = Parser.parse(src, {'locations': true, 'sourceType': sourceType,
                                'ecmaVersion': '2020'})

// process.stdout.write(JSON.stringify(tree))

const variables = []
const scopes = []

function walk(node, parent) {
    if (node.type === 'VariableDeclaration') {
        node.declarations.forEach(decl => {
            variables.push(decl.id.name)
        })
    }

    for (let key in node) {
        if (node[key] && typeof node[key] === 'object') {
            walk(node[key], node)
        }
    }

    if (node.type === 'BlockStatement' || node.type === 'FunctionDeclaration' || node.type === 'FunctionExpression' || node.type === 'Program') {
        scopes.pop()
    }
}

walk(tree)

process.stdout.write(variables.toString())