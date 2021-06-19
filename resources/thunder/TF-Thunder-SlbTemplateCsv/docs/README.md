# TF::Thunder::SlbTemplateCsv

`thunder_slb_template_csv` provides details about slb template csv

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateCsv",
    "Properties" : {
        "<a href="#csvname" title="CsvName">CsvName</a>" : <i>String</i>,
        "<a href="#delimchar" title="DelimChar">DelimChar</a>" : <i>String</i>,
        "<a href="#delimnum" title="DelimNum">DelimNum</a>" : <i>Double</i>,
        "<a href="#ipv6enable" title="Ipv6Enable">Ipv6Enable</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#multiplefields" title="MultipleFields">MultipleFields</a>" : <i>[ <a href="multiplefieldsdefinition.md">MultipleFieldsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateCsv
Properties:
    <a href="#csvname" title="CsvName">CsvName</a>: <i>String</i>
    <a href="#delimchar" title="DelimChar">DelimChar</a>: <i>String</i>
    <a href="#delimnum" title="DelimNum">DelimNum</a>: <i>Double</i>
    <a href="#ipv6enable" title="Ipv6Enable">Ipv6Enable</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#multiplefields" title="MultipleFields">MultipleFields</a>: <i>
      - <a href="multiplefieldsdefinition.md">MultipleFieldsDefinition</a></i>
</pre>

## Properties

#### CsvName

Specify name of csv template.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelimChar

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelimNum

enter a delimiter number, default 44 (“,”).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Enable

Support IPv6 IP ranges.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultipleFields

_Required_: No

_Type_: List of <a href="multiplefieldsdefinition.md">MultipleFieldsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

