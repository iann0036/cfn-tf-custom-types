# TF::Cloudsmith::Entitlement

CloudFormation equivalent of cloudsmith_entitlement

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudsmith::Entitlement",
    "Properties" : {
        "<a href="#isactive" title="IsActive">IsActive</a>" : <i>Boolean</i>,
        "<a href="#limitdaterangefrom" title="LimitDateRangeFrom">LimitDateRangeFrom</a>" : <i>String</i>,
        "<a href="#limitdaterangeto" title="LimitDateRangeTo">LimitDateRangeTo</a>" : <i>String</i>,
        "<a href="#limitnumclients" title="LimitNumClients">LimitNumClients</a>" : <i>Double</i>,
        "<a href="#limitnumdownloads" title="LimitNumDownloads">LimitNumDownloads</a>" : <i>Double</i>,
        "<a href="#limitpackagequery" title="LimitPackageQuery">LimitPackageQuery</a>" : <i>String</i>,
        "<a href="#limitpathquery" title="LimitPathQuery">LimitPathQuery</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudsmith::Entitlement
Properties:
    <a href="#isactive" title="IsActive">IsActive</a>: <i>Boolean</i>
    <a href="#limitdaterangefrom" title="LimitDateRangeFrom">LimitDateRangeFrom</a>: <i>String</i>
    <a href="#limitdaterangeto" title="LimitDateRangeTo">LimitDateRangeTo</a>: <i>String</i>
    <a href="#limitnumclients" title="LimitNumClients">LimitNumClients</a>: <i>Double</i>
    <a href="#limitnumdownloads" title="LimitNumDownloads">LimitNumDownloads</a>: <i>Double</i>
    <a href="#limitpackagequery" title="LimitPackageQuery">LimitPackageQuery</a>: <i>String</i>
    <a href="#limitpathquery" title="LimitPathQuery">LimitPathQuery</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
</pre>

## Properties

#### IsActive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitDateRangeFrom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitDateRangeTo

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitNumClients

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitNumDownloads

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitPackageQuery

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitPathQuery

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

_Required_: No

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

#### Id

Returns the <code>Id</code> value.

