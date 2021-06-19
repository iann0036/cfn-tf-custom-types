# TF::Thunder::VrrpVrid

`thunder_vrrp_vrid` Provides details about thunder vrrp vrid

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::VrrpVrid",
    "Properties" : {
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vridval" title="VridVal">VridVal</a>" : <i>Double</i>,
        "<a href="#bladeparameters" title="BladeParameters">BladeParameters</a>" : <i>[ <a href="bladeparametersdefinition.md">BladeParametersDefinition</a>, ... ]</i>,
        "<a href="#floatingip" title="FloatingIp">FloatingIp</a>" : <i>[ <a href="floatingipdefinition.md">FloatingIpDefinition</a>, ... ]</i>,
        "<a href="#follow" title="Follow">Follow</a>" : <i>[ <a href="followdefinition.md">FollowDefinition</a>, ... ]</i>,
        "<a href="#preemptmode" title="PreemptMode">PreemptMode</a>" : <i>[ <a href="preemptmodedefinition.md">PreemptModeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::VrrpVrid
Properties:
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vridval" title="VridVal">VridVal</a>: <i>Double</i>
    <a href="#bladeparameters" title="BladeParameters">BladeParameters</a>: <i>
      - <a href="bladeparametersdefinition.md">BladeParametersDefinition</a></i>
    <a href="#floatingip" title="FloatingIp">FloatingIp</a>: <i>
      - <a href="floatingipdefinition.md">FloatingIpDefinition</a></i>
    <a href="#follow" title="Follow">Follow</a>: <i>
      - <a href="followdefinition.md">FollowDefinition</a></i>
    <a href="#preemptmode" title="PreemptMode">PreemptMode</a>: <i>
      - <a href="preemptmodedefinition.md">PreemptModeDefinition</a></i>
</pre>

## Properties

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VridVal

Specify ha VRRP-A vrid.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BladeParameters

_Required_: No

_Type_: List of <a href="bladeparametersdefinition.md">BladeParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIp

_Required_: No

_Type_: List of <a href="floatingipdefinition.md">FloatingIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Follow

_Required_: No

_Type_: List of <a href="followdefinition.md">FollowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreemptMode

_Required_: No

_Type_: List of <a href="preemptmodedefinition.md">PreemptModeDefinition</a>

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

