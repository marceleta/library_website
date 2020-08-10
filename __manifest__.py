{
    'name':'Library Website',
    'description':'Create and check book checkout requests.',
    'author':'Daniel Reis',
    'depends':['library_checkout'],
    'data':[
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/library_member.xml',
    ],
}