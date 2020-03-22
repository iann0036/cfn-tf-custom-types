# Terraform::Nomad::QuotaSpecification

Manages a quota specification in a Nomad cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Nomad::QuotaSpecification",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#limits" title="Limits">Limits</a>" : <i>[ <a href="limits.md">Limits</a>, ... ]</i>,
        "<a href="#regionlimit" title="RegionLimit">RegionLimit</a>" : <i>[ <a href="regionlimit.md">RegionLimit</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Nomad::QuotaSpecification
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#limits" title="Limits">Limits</a>: <i>
      - <a href="limits.md">Limits</a></i>
    <a href="#regionlimit" title="RegionLimit">RegionLimit</a>: <i>
      - <a href="regionlimit.md">RegionLimit</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limits

_Required_: No

_Type_: List of <a href="limits.md">Limits</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionLimit

_Required_: No

_Type_: List of <a href="regionlimit.md">RegionLimit</a>

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

