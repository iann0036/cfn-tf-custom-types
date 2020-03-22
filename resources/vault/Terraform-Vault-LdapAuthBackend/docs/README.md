# Terraform::Vault::LdapAuthBackend

Provides a resource for managing an [LDAP auth backend within Vault](https://www.vaultproject.io/docs/auth/ldap.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::LdapAuthBackend",
    "Properties" : {
        "<a href="#binddn" title="Binddn">Binddn</a>" : <i>String</i>,
        "<a href="#bindpass" title="Bindpass">Bindpass</a>" : <i>String</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
        "<a href="#denynullbind" title="DenyNullBind">DenyNullBind</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#discoverdn" title="Discoverdn">Discoverdn</a>" : <i>Boolean</i>,
        "<a href="#groupattr" title="Groupattr">Groupattr</a>" : <i>String</i>,
        "<a href="#groupdn" title="Groupdn">Groupdn</a>" : <i>String</i>,
        "<a href="#groupfilter" title="Groupfilter">Groupfilter</a>" : <i>String</i>,
        "<a href="#insecuretls" title="InsecureTls">InsecureTls</a>" : <i>Boolean</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#starttls" title="Starttls">Starttls</a>" : <i>Boolean</i>,
        "<a href="#tlsmaxversion" title="TlsMaxVersion">TlsMaxVersion</a>" : <i>String</i>,
        "<a href="#tlsminversion" title="TlsMinVersion">TlsMinVersion</a>" : <i>String</i>,
        "<a href="#tokenboundcidrs" title="TokenBoundCidrs">TokenBoundCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#tokenexplicitmaxttl" title="TokenExplicitMaxTtl">TokenExplicitMaxTtl</a>" : <i>Double</i>,
        "<a href="#tokenmaxttl" title="TokenMaxTtl">TokenMaxTtl</a>" : <i>Double</i>,
        "<a href="#tokennodefaultpolicy" title="TokenNoDefaultPolicy">TokenNoDefaultPolicy</a>" : <i>Boolean</i>,
        "<a href="#tokennumuses" title="TokenNumUses">TokenNumUses</a>" : <i>Double</i>,
        "<a href="#tokenperiod" title="TokenPeriod">TokenPeriod</a>" : <i>Double</i>,
        "<a href="#tokenpolicies" title="TokenPolicies">TokenPolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#tokenttl" title="TokenTtl">TokenTtl</a>" : <i>Double</i>,
        "<a href="#tokentype" title="TokenType">TokenType</a>" : <i>String</i>,
        "<a href="#upndomain" title="Upndomain">Upndomain</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#usetokengroups" title="UseTokenGroups">UseTokenGroups</a>" : <i>Boolean</i>,
        "<a href="#userattr" title="Userattr">Userattr</a>" : <i>String</i>,
        "<a href="#userdn" title="Userdn">Userdn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::LdapAuthBackend
Properties:
    <a href="#binddn" title="Binddn">Binddn</a>: <i>String</i>
    <a href="#bindpass" title="Bindpass">Bindpass</a>: <i>String</i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
    <a href="#denynullbind" title="DenyNullBind">DenyNullBind</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#discoverdn" title="Discoverdn">Discoverdn</a>: <i>Boolean</i>
    <a href="#groupattr" title="Groupattr">Groupattr</a>: <i>String</i>
    <a href="#groupdn" title="Groupdn">Groupdn</a>: <i>String</i>
    <a href="#groupfilter" title="Groupfilter">Groupfilter</a>: <i>String</i>
    <a href="#insecuretls" title="InsecureTls">InsecureTls</a>: <i>Boolean</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#starttls" title="Starttls">Starttls</a>: <i>Boolean</i>
    <a href="#tlsmaxversion" title="TlsMaxVersion">TlsMaxVersion</a>: <i>String</i>
    <a href="#tlsminversion" title="TlsMinVersion">TlsMinVersion</a>: <i>String</i>
    <a href="#tokenboundcidrs" title="TokenBoundCidrs">TokenBoundCidrs</a>: <i>
      - String</i>
    <a href="#tokenexplicitmaxttl" title="TokenExplicitMaxTtl">TokenExplicitMaxTtl</a>: <i>Double</i>
    <a href="#tokenmaxttl" title="TokenMaxTtl">TokenMaxTtl</a>: <i>Double</i>
    <a href="#tokennodefaultpolicy" title="TokenNoDefaultPolicy">TokenNoDefaultPolicy</a>: <i>Boolean</i>
    <a href="#tokennumuses" title="TokenNumUses">TokenNumUses</a>: <i>Double</i>
    <a href="#tokenperiod" title="TokenPeriod">TokenPeriod</a>: <i>Double</i>
    <a href="#tokenpolicies" title="TokenPolicies">TokenPolicies</a>: <i>
      - String</i>
    <a href="#tokenttl" title="TokenTtl">TokenTtl</a>: <i>Double</i>
    <a href="#tokentype" title="TokenType">TokenType</a>: <i>String</i>
    <a href="#upndomain" title="Upndomain">Upndomain</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#usetokengroups" title="UseTokenGroups">UseTokenGroups</a>: <i>Boolean</i>
    <a href="#userattr" title="Userattr">Userattr</a>: <i>String</i>
    <a href="#userdn" title="Userdn">Userdn</a>: <i>String</i>
</pre>

## Properties

#### Binddn

DN of object to bind when performing user search.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bindpass

Password to use with `binddn` when performing user search.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

Trusted CA to validate TLS certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DenyNullBind

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for the LDAP auth backend mount.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Discoverdn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groupattr

LDAP attribute to follow on objects returned by groupfilter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groupdn

Base DN under which to perform group search.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groupfilter

Go template used to construct group membership query.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsecureTls

Control whether or TLS certificates must be validated.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Path to mount the LDAP auth backend under.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Starttls

Control use of TLS when conecting to LDAP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsMaxVersion

Maximum acceptable version of TLS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsMinVersion

Minimum acceptable version of TLS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenBoundCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenExplicitMaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenMaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenNoDefaultPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenNumUses

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenPolicies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Upndomain

The userPrincipalDomain used to construct UPN string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

The URL of the LDAP server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseTokenGroups

Use the Active Directory tokenGroups constructed attribute of the user to find the group memberships.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Userattr

Attribute on user object matching username passed in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Userdn

Base DN under which to perform user search.

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

#### Accessor

Returns the <code>Accessor</code> value.

#### Id

Returns the <code>Id</code> value.

