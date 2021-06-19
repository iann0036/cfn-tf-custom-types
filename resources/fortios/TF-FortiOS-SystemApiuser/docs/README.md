# TF::FortiOS::SystemApiuser

Configure API users.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemApiuser",
    "Properties" : {
        "<a href="#accprofile" title="Accprofile">Accprofile</a>" : <i>String</i>,
        "<a href="#apikey" title="ApiKey">ApiKey</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#corsalloworigin" title="CorsAllowOrigin">CorsAllowOrigin</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#peerauth" title="PeerAuth">PeerAuth</a>" : <i>String</i>,
        "<a href="#peergroup" title="PeerGroup">PeerGroup</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#trusthost" title="Trusthost">Trusthost</a>" : <i>[ <a href="trusthostdefinition.md">TrusthostDefinition</a>, ... ]</i>,
        "<a href="#vdom" title="Vdom">Vdom</a>" : <i>[ <a href="vdomdefinition.md">VdomDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemApiuser
Properties:
    <a href="#accprofile" title="Accprofile">Accprofile</a>: <i>String</i>
    <a href="#apikey" title="ApiKey">ApiKey</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#corsalloworigin" title="CorsAllowOrigin">CorsAllowOrigin</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#peerauth" title="PeerAuth">PeerAuth</a>: <i>String</i>
    <a href="#peergroup" title="PeerGroup">PeerGroup</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#trusthost" title="Trusthost">Trusthost</a>: <i>
      - <a href="trusthostdefinition.md">TrusthostDefinition</a></i>
    <a href="#vdom" title="Vdom">Vdom</a>: <i>
      - <a href="vdomdefinition.md">VdomDefinition</a></i>
</pre>

## Properties

#### Accprofile

Admin user access profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiKey

Admin user password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsAllowOrigin

Value for Access-Control-Allow-Origin on API responses. Avoid using '*' if possible.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

User name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAuth

Enable/disable peer authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerGroup

Peer group name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

Schedule name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost

_Required_: No

_Type_: List of <a href="trusthostdefinition.md">TrusthostDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdom

_Required_: No

_Type_: List of <a href="vdomdefinition.md">VdomDefinition</a>

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

