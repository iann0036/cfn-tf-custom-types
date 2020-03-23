# Terraform::AWS::Route53Zone

Manages a Route53 Hosted Zone.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Route53Zone",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#delegationsetid" title="DelegationSetId">DelegationSetId</a>" : <i>String</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpcregion" title="VpcRegion">VpcRegion</a>" : <i>String</i>,
        "<a href="#vpc" title="Vpc">Vpc</a>" : <i>[ <a href="vpc.md">Vpc</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Route53Zone
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#delegationsetid" title="DelegationSetId">DelegationSetId</a>: <i>String</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vpcregion" title="VpcRegion">VpcRegion</a>: <i>String</i>
    <a href="#vpc" title="Vpc">Vpc</a>: <i>
      - <a href="vpc.md">Vpc</a></i>
</pre>

## Properties

#### Comment

A comment for the hosted zone. Defaults to 'Managed by Terraform'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelegationSetId

The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

Whether to destroy all records (possibly managed outside of Terraform) in the zone when destroying the zone.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

This is the name of the hosted zone.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the zone.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc

_Required_: No

_Type_: List of <a href="vpc.md">Vpc</a>

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

#### NameServers

Returns the <code>NameServers</code> value.

#### ZoneId

Returns the <code>ZoneId</code> value.

