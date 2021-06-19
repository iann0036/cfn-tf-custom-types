# TF::Rancher2::AuthConfigFreeipa

CloudFormation equivalent of rancher2_auth_config_freeipa

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Rancher2::AuthConfigFreeipa",
    "Properties" : {
        "<a href="#accessmode" title="AccessMode">AccessMode</a>" : <i>String</i>,
        "<a href="#allowedprincipalids" title="AllowedPrincipalIds">AllowedPrincipalIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
        "<a href="#connectiontimeout" title="ConnectionTimeout">ConnectionTimeout</a>" : <i>Double</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#groupdnattribute" title="GroupDnAttribute">GroupDnAttribute</a>" : <i>String</i>,
        "<a href="#groupmembermappingattribute" title="GroupMemberMappingAttribute">GroupMemberMappingAttribute</a>" : <i>String</i>,
        "<a href="#groupmemberuserattribute" title="GroupMemberUserAttribute">GroupMemberUserAttribute</a>" : <i>String</i>,
        "<a href="#groupnameattribute" title="GroupNameAttribute">GroupNameAttribute</a>" : <i>String</i>,
        "<a href="#groupobjectclass" title="GroupObjectClass">GroupObjectClass</a>" : <i>String</i>,
        "<a href="#groupsearchattribute" title="GroupSearchAttribute">GroupSearchAttribute</a>" : <i>String</i>,
        "<a href="#groupsearchbase" title="GroupSearchBase">GroupSearchBase</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#nestedgroupmembershipenabled" title="NestedGroupMembershipEnabled">NestedGroupMembershipEnabled</a>" : <i>Boolean</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#servers" title="Servers">Servers</a>" : <i>[ String, ... ]</i>,
        "<a href="#serviceaccountdistinguishedname" title="ServiceAccountDistinguishedName">ServiceAccountDistinguishedName</a>" : <i>String</i>,
        "<a href="#serviceaccountpassword" title="ServiceAccountPassword">ServiceAccountPassword</a>" : <i>String</i>,
        "<a href="#testpassword" title="TestPassword">TestPassword</a>" : <i>String</i>,
        "<a href="#testusername" title="TestUsername">TestUsername</a>" : <i>String</i>,
        "<a href="#tls" title="Tls">Tls</a>" : <i>Boolean</i>,
        "<a href="#userdisabledbitmask" title="UserDisabledBitMask">UserDisabledBitMask</a>" : <i>Double</i>,
        "<a href="#userenabledattribute" title="UserEnabledAttribute">UserEnabledAttribute</a>" : <i>String</i>,
        "<a href="#userloginattribute" title="UserLoginAttribute">UserLoginAttribute</a>" : <i>String</i>,
        "<a href="#usermemberattribute" title="UserMemberAttribute">UserMemberAttribute</a>" : <i>String</i>,
        "<a href="#usernameattribute" title="UserNameAttribute">UserNameAttribute</a>" : <i>String</i>,
        "<a href="#userobjectclass" title="UserObjectClass">UserObjectClass</a>" : <i>String</i>,
        "<a href="#usersearchattribute" title="UserSearchAttribute">UserSearchAttribute</a>" : <i>String</i>,
        "<a href="#usersearchbase" title="UserSearchBase">UserSearchBase</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Rancher2::AuthConfigFreeipa
Properties:
    <a href="#accessmode" title="AccessMode">AccessMode</a>: <i>String</i>
    <a href="#allowedprincipalids" title="AllowedPrincipalIds">AllowedPrincipalIds</a>: <i>
      - String</i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
    <a href="#connectiontimeout" title="ConnectionTimeout">ConnectionTimeout</a>: <i>Double</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#groupdnattribute" title="GroupDnAttribute">GroupDnAttribute</a>: <i>String</i>
    <a href="#groupmembermappingattribute" title="GroupMemberMappingAttribute">GroupMemberMappingAttribute</a>: <i>String</i>
    <a href="#groupmemberuserattribute" title="GroupMemberUserAttribute">GroupMemberUserAttribute</a>: <i>String</i>
    <a href="#groupnameattribute" title="GroupNameAttribute">GroupNameAttribute</a>: <i>String</i>
    <a href="#groupobjectclass" title="GroupObjectClass">GroupObjectClass</a>: <i>String</i>
    <a href="#groupsearchattribute" title="GroupSearchAttribute">GroupSearchAttribute</a>: <i>String</i>
    <a href="#groupsearchbase" title="GroupSearchBase">GroupSearchBase</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#nestedgroupmembershipenabled" title="NestedGroupMembershipEnabled">NestedGroupMembershipEnabled</a>: <i>Boolean</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#servers" title="Servers">Servers</a>: <i>
      - String</i>
    <a href="#serviceaccountdistinguishedname" title="ServiceAccountDistinguishedName">ServiceAccountDistinguishedName</a>: <i>String</i>
    <a href="#serviceaccountpassword" title="ServiceAccountPassword">ServiceAccountPassword</a>: <i>String</i>
    <a href="#testpassword" title="TestPassword">TestPassword</a>: <i>String</i>
    <a href="#testusername" title="TestUsername">TestUsername</a>: <i>String</i>
    <a href="#tls" title="Tls">Tls</a>: <i>Boolean</i>
    <a href="#userdisabledbitmask" title="UserDisabledBitMask">UserDisabledBitMask</a>: <i>Double</i>
    <a href="#userenabledattribute" title="UserEnabledAttribute">UserEnabledAttribute</a>: <i>String</i>
    <a href="#userloginattribute" title="UserLoginAttribute">UserLoginAttribute</a>: <i>String</i>
    <a href="#usermemberattribute" title="UserMemberAttribute">UserMemberAttribute</a>: <i>String</i>
    <a href="#usernameattribute" title="UserNameAttribute">UserNameAttribute</a>: <i>String</i>
    <a href="#userobjectclass" title="UserObjectClass">UserObjectClass</a>: <i>String</i>
    <a href="#usersearchattribute" title="UserSearchAttribute">UserSearchAttribute</a>: <i>String</i>
    <a href="#usersearchbase" title="UserSearchBase">UserSearchBase</a>: <i>String</i>
</pre>

## Properties

#### AccessMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedPrincipalIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupDnAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupMemberMappingAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupMemberUserAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupNameAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupObjectClass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupSearchAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupSearchBase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NestedGroupMembershipEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Servers

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountDistinguishedName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountPassword

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestPassword

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestUsername

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tls

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDisabledBitMask

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserEnabledAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserLoginAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserMemberAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserNameAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserObjectClass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserSearchAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserSearchBase

_Required_: Yes

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

#### Name

Returns the <code>Name</code> value.

#### Type

Returns the <code>Type</code> value.

