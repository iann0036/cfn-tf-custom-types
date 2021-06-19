# TF::FortiOS::UserPeer

Configure peer users.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::UserPeer",
    "Properties" : {
        "<a href="#ca" title="Ca">Ca</a>" : <i>String</i>,
        "<a href="#cn" title="Cn">Cn</a>" : <i>String</i>,
        "<a href="#cntype" title="CnType">CnType</a>" : <i>String</i>,
        "<a href="#ldapmode" title="LdapMode">LdapMode</a>" : <i>String</i>,
        "<a href="#ldappassword" title="LdapPassword">LdapPassword</a>" : <i>String</i>,
        "<a href="#ldapserver" title="LdapServer">LdapServer</a>" : <i>String</i>,
        "<a href="#ldapusername" title="LdapUsername">LdapUsername</a>" : <i>String</i>,
        "<a href="#mandatorycaverify" title="MandatoryCaVerify">MandatoryCaVerify</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ocspoverrideserver" title="OcspOverrideServer">OcspOverrideServer</a>" : <i>String</i>,
        "<a href="#passwd" title="Passwd">Passwd</a>" : <i>String</i>,
        "<a href="#subject" title="Subject">Subject</a>" : <i>String</i>,
        "<a href="#twofactor" title="TwoFactor">TwoFactor</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::UserPeer
Properties:
    <a href="#ca" title="Ca">Ca</a>: <i>String</i>
    <a href="#cn" title="Cn">Cn</a>: <i>String</i>
    <a href="#cntype" title="CnType">CnType</a>: <i>String</i>
    <a href="#ldapmode" title="LdapMode">LdapMode</a>: <i>String</i>
    <a href="#ldappassword" title="LdapPassword">LdapPassword</a>: <i>String</i>
    <a href="#ldapserver" title="LdapServer">LdapServer</a>: <i>String</i>
    <a href="#ldapusername" title="LdapUsername">LdapUsername</a>: <i>String</i>
    <a href="#mandatorycaverify" title="MandatoryCaVerify">MandatoryCaVerify</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ocspoverrideserver" title="OcspOverrideServer">OcspOverrideServer</a>: <i>String</i>
    <a href="#passwd" title="Passwd">Passwd</a>: <i>String</i>
    <a href="#subject" title="Subject">Subject</a>: <i>String</i>
    <a href="#twofactor" title="TwoFactor">TwoFactor</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Ca

Name of the CA certificate as returned by the execute vpn certificate ca list command.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cn

Peer certificate common name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CnType

Peer certificate common name type. Valid values: `string`, `email`, `FQDN`, `ipv4`, `ipv6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapMode

Mode for LDAP peer authentication. Valid values: `password`, `principal-name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapPassword

Password for LDAP server bind.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapServer

Name of an LDAP server defined under the user ldap command. Performs client access rights check.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapUsername

Username for LDAP server bind.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MandatoryCaVerify

Determine what happens to the peer if the CA certificate is not installed. Disable to automatically consider the peer certificate as valid. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Peer name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspOverrideServer

Online Certificate Status Protocol (OCSP) server for certificate retrieval.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passwd

Peer's password used for two-factor authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

Peer certificate name constraints.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TwoFactor

Enable/disable two-factor authentication, applying certificate and password-based authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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

