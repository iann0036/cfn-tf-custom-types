# TF::Constellix::CnameRecordPool

Manages the pools of CNAME records.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Constellix::CnameRecordPool",
    "Properties" : {
        "<a href="#disableflag" title="DisableFlag">DisableFlag</a>" : <i>String</i>,
        "<a href="#failedflag" title="FailedFlag">FailedFlag</a>" : <i>String</i>,
        "<a href="#minavailablefailover" title="MinAvailableFailover">MinAvailableFailover</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#note" title="Note">Note</a>" : <i>String</i>,
        "<a href="#numreturn" title="NumReturn">NumReturn</a>" : <i>Double</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
        "<a href="#values" title="Values">Values</a>" : <i>[ <a href="valuesdefinition.md">ValuesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Constellix::CnameRecordPool
Properties:
    <a href="#disableflag" title="DisableFlag">DisableFlag</a>: <i>String</i>
    <a href="#failedflag" title="FailedFlag">FailedFlag</a>: <i>String</i>
    <a href="#minavailablefailover" title="MinAvailableFailover">MinAvailableFailover</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#note" title="Note">Note</a>: <i>String</i>
    <a href="#numreturn" title="NumReturn">NumReturn</a>: <i>Double</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
    <a href="#values" title="Values">Values</a>: <i>
      - <a href="valuesdefinition.md">ValuesDefinition</a></i>
</pre>

## Properties

#### DisableFlag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailedFlag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinAvailableFailover

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Note

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumReturn

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Values

_Required_: No

_Type_: List of <a href="valuesdefinition.md">ValuesDefinition</a>

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

