# TF::FortiOS::AuthenticationScheme

Configure Authentication Schemes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::AuthenticationScheme",
    "Properties" : {
        "<a href="#domaincontroller" title="DomainController">DomainController</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#fssoagentforntlm" title="FssoAgentForNtlm">FssoAgentForNtlm</a>" : <i>String</i>,
        "<a href="#fssoguest" title="FssoGuest">FssoGuest</a>" : <i>String</i>,
        "<a href="#kerberoskeytab" title="KerberosKeytab">KerberosKeytab</a>" : <i>String</i>,
        "<a href="#method" title="Method">Method</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#negotiatentlm" title="NegotiateNtlm">NegotiateNtlm</a>" : <i>String</i>,
        "<a href="#requiretfa" title="RequireTfa">RequireTfa</a>" : <i>String</i>,
        "<a href="#sshca" title="SshCa">SshCa</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#userdatabase" title="UserDatabase">UserDatabase</a>" : <i>[ <a href="userdatabasedefinition.md">UserDatabaseDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::AuthenticationScheme
Properties:
    <a href="#domaincontroller" title="DomainController">DomainController</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#fssoagentforntlm" title="FssoAgentForNtlm">FssoAgentForNtlm</a>: <i>String</i>
    <a href="#fssoguest" title="FssoGuest">FssoGuest</a>: <i>String</i>
    <a href="#kerberoskeytab" title="KerberosKeytab">KerberosKeytab</a>: <i>String</i>
    <a href="#method" title="Method">Method</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#negotiatentlm" title="NegotiateNtlm">NegotiateNtlm</a>: <i>String</i>
    <a href="#requiretfa" title="RequireTfa">RequireTfa</a>: <i>String</i>
    <a href="#sshca" title="SshCa">SshCa</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#userdatabase" title="UserDatabase">UserDatabase</a>: <i>
      - <a href="userdatabasedefinition.md">UserDatabaseDefinition</a></i>
</pre>

## Properties

#### DomainController

Domain controller setting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FssoAgentForNtlm

FSSO agent to use for NTLM authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FssoGuest

Enable/disable user fsso-guest authentication (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KerberosKeytab

Kerberos keytab setting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

Authentication methods (default = basic). Valid values: `ntlm`, `basic`, `digest`, `form`, `negotiate`, `fsso`, `rsso`, `ssh-publickey`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Authentication scheme name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegotiateNtlm

Enable/disable negotiate authentication for NTLM (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireTfa

Enable/disable two-factor authentication (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshCa

SSH CA name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDatabase

_Required_: No

_Type_: List of <a href="userdatabasedefinition.md">UserDatabaseDefinition</a>

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

