# TF::Aviatrix::VpnProfile

The **aviatrix_vpn_profile** resource allows the creation and management of Aviatrix VPN user profiles.

~> **NOTE:** As of R2.15, management of user/profile attachment can be set using `manage_user_attachment`. This argument must be set to *true* in either **aviatrix_vpn_user** or **aviatrix_vpn_profile**. If attachment is managed in the **aviatrix_vpn_profile** (set to *true*), it must be set to *false* in the **aviatrix_vpn_user** resource and vice versa.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::VpnProfile",
    "Properties" : {
        "<a href="#baserule" title="BaseRule">BaseRule</a>" : <i>String</i>,
        "<a href="#manageuserattachment" title="ManageUserAttachment">ManageUserAttachment</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ String, ... ]</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>[ <a href="policydefinition.md">PolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::VpnProfile
Properties:
    <a href="#baserule" title="BaseRule">BaseRule</a>: <i>String</i>
    <a href="#manageuserattachment" title="ManageUserAttachment">ManageUserAttachment</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#users" title="Users">Users</a>: <i>
      - String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>
      - <a href="policydefinition.md">PolicyDefinition</a></i>
</pre>

## Properties

#### BaseRule

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageUserAttachment

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: No

_Type_: List of <a href="policydefinition.md">PolicyDefinition</a>

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

