# TF::FortiOS::VpnsslSettings AuthenticationRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#auth" title="Auth">Auth</a>" : <i>String</i>,
    "<a href="#cipher" title="Cipher">Cipher</a>" : <i>String</i>,
    "<a href="#clientcert" title="ClientCert">ClientCert</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#portal" title="Portal">Portal</a>" : <i>String</i>,
    "<a href="#realm" title="Realm">Realm</a>" : <i>String</i>,
    "<a href="#sourceaddress6negate" title="SourceAddress6Negate">SourceAddress6Negate</a>" : <i>String</i>,
    "<a href="#sourceaddressnegate" title="SourceAddressNegate">SourceAddressNegate</a>" : <i>String</i>,
    "<a href="#userpeer" title="UserPeer">UserPeer</a>" : <i>String</i>,
    "<a href="#groups" title="Groups">Groups</a>" : <i>[ <a href="groupsdefinition.md">GroupsDefinition</a>, ... ]</i>,
    "<a href="#sourceaddress" title="SourceAddress">SourceAddress</a>" : <i>[ <a href="sourceaddressdefinition.md">SourceAddressDefinition</a>, ... ]</i>,
    "<a href="#sourceaddress6" title="SourceAddress6">SourceAddress6</a>" : <i>[ <a href="sourceaddress6definition.md">SourceAddress6Definition</a>, ... ]</i>,
    "<a href="#sourceinterface" title="SourceInterface">SourceInterface</a>" : <i>[ <a href="sourceinterfacedefinition.md">SourceInterfaceDefinition</a>, ... ]</i>,
    "<a href="#users" title="Users">Users</a>" : <i>[ <a href="usersdefinition.md">UsersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#auth" title="Auth">Auth</a>: <i>String</i>
<a href="#cipher" title="Cipher">Cipher</a>: <i>String</i>
<a href="#clientcert" title="ClientCert">ClientCert</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#portal" title="Portal">Portal</a>: <i>String</i>
<a href="#realm" title="Realm">Realm</a>: <i>String</i>
<a href="#sourceaddress6negate" title="SourceAddress6Negate">SourceAddress6Negate</a>: <i>String</i>
<a href="#sourceaddressnegate" title="SourceAddressNegate">SourceAddressNegate</a>: <i>String</i>
<a href="#userpeer" title="UserPeer">UserPeer</a>: <i>String</i>
<a href="#groups" title="Groups">Groups</a>: <i>
      - <a href="groupsdefinition.md">GroupsDefinition</a></i>
<a href="#sourceaddress" title="SourceAddress">SourceAddress</a>: <i>
      - <a href="sourceaddressdefinition.md">SourceAddressDefinition</a></i>
<a href="#sourceaddress6" title="SourceAddress6">SourceAddress6</a>: <i>
      - <a href="sourceaddress6definition.md">SourceAddress6Definition</a></i>
<a href="#sourceinterface" title="SourceInterface">SourceInterface</a>: <i>
      - <a href="sourceinterfacedefinition.md">SourceInterfaceDefinition</a></i>
<a href="#users" title="Users">Users</a>: <i>
      - <a href="usersdefinition.md">UsersDefinition</a></i>
</pre>

## Properties

#### Auth

SSL VPN authentication method restriction. Valid values: `any`, `local`, `radius`, `tacacs+`, `ldap`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cipher

SSL VPN cipher strength. Valid values: `any`, `high`, `medium`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCert

Enable/disable SSL VPN client certificate restrictive. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID (0 - 4294967295).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Portal

SSL VPN portal.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Realm

SSL VPN realm.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddress6Negate

Enable/disable negated source IPv6 address match. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddressNegate

Enable/disable negated source address match. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPeer

Name of user peer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

_Required_: No

_Type_: List of <a href="groupsdefinition.md">GroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddress

_Required_: No

_Type_: List of <a href="sourceaddressdefinition.md">SourceAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddress6

_Required_: No

_Type_: List of <a href="sourceaddress6definition.md">SourceAddress6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceInterface

_Required_: No

_Type_: List of <a href="sourceinterfacedefinition.md">SourceInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

_Required_: No

_Type_: List of <a href="usersdefinition.md">UsersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

