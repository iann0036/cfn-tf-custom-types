# Terraform::Alicloud::DbDatabase

Provides an RDS database resource. A DB database deployed in a DB instance. A DB instance can own multiple databases.

-> **NOTE:** This resource does not support creating 'PPAS' database. You have to login RDS instance to create manually.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::DbDatabase",
    "Properties" : {
        "<a href="#characterset" title="CharacterSet">CharacterSet</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::DbDatabase
Properties:
    <a href="#characterset" title="CharacterSet">CharacterSet</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### CharacterSet

Character set. The value range is limited to the following:
- MySQL: [ utf8, gbk, latin1, utf8mb4 ] \(`utf8mb4` only supports versions 5.5 and 5.6\).
- SQLServer: [ Chinese_PRC_CI_AS, Chinese_PRC_CS_AS, SQL_Latin1_General_CP1_CI_AS, SQL_Latin1_General_CP1_CS_AS, Chinese_PRC_BIN ]
- PostgreSQL: [ KOI8U、UTF8、WIN866、WIN874、WIN1250、WIN1251、WIN1252、WIN1253、WIN1254、WIN1255、WIN1256、WIN1257、WIN1258、EUC_CN、EUC_KR、EUC_TW、EUC_JP、EUC_JIS_2004、KOI8R、MULE_INTERNAL、LATIN1、LATIN2、LATIN3、LATIN4、LATIN5、LATIN6、LATIN7、LATIN8、LATIN9、LATIN10、ISO_8859_5、ISO_8859_6、ISO_8859_7、ISO_8859_8、SQL_ASCII ].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Database description. It cannot begin with https://. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The Id of instance that can run database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the database requiring a uniqueness check. It may consist of lower case letters, numbers, and underlines, and must start with a letter
and have no more than 64 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

