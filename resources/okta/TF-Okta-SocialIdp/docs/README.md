# TF::Okta::SocialIdp

CloudFormation equivalent of okta_social_idp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::SocialIdp",
    "Properties" : {
        "<a href="#accountlinkaction" title="AccountLinkAction">AccountLinkAction</a>" : <i>String</i>,
        "<a href="#accountlinkgroupinclude" title="AccountLinkGroupInclude">AccountLinkGroupInclude</a>" : <i>[ String, ... ]</i>,
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#clientsecret" title="ClientSecret">ClientSecret</a>" : <i>String</i>,
        "<a href="#deprovisionedaction" title="DeprovisionedAction">DeprovisionedAction</a>" : <i>String</i>,
        "<a href="#groupsaction" title="GroupsAction">GroupsAction</a>" : <i>String</i>,
        "<a href="#groupsassignment" title="GroupsAssignment">GroupsAssignment</a>" : <i>[ String, ... ]</i>,
        "<a href="#groupsattribute" title="GroupsAttribute">GroupsAttribute</a>" : <i>String</i>,
        "<a href="#groupsfilter" title="GroupsFilter">GroupsFilter</a>" : <i>[ String, ... ]</i>,
        "<a href="#issuermode" title="IssuerMode">IssuerMode</a>" : <i>String</i>,
        "<a href="#matchattribute" title="MatchAttribute">MatchAttribute</a>" : <i>String</i>,
        "<a href="#matchtype" title="MatchType">MatchType</a>" : <i>String</i>,
        "<a href="#maxclockskew" title="MaxClockSkew">MaxClockSkew</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#profilemaster" title="ProfileMaster">ProfileMaster</a>" : <i>Boolean</i>,
        "<a href="#protocoltype" title="ProtocolType">ProtocolType</a>" : <i>String</i>,
        "<a href="#provisioningaction" title="ProvisioningAction">ProvisioningAction</a>" : <i>String</i>,
        "<a href="#requestsignaturealgorithm" title="RequestSignatureAlgorithm">RequestSignatureAlgorithm</a>" : <i>String</i>,
        "<a href="#requestsignaturescope" title="RequestSignatureScope">RequestSignatureScope</a>" : <i>String</i>,
        "<a href="#responsesignaturealgorithm" title="ResponseSignatureAlgorithm">ResponseSignatureAlgorithm</a>" : <i>String</i>,
        "<a href="#responsesignaturescope" title="ResponseSignatureScope">ResponseSignatureScope</a>" : <i>String</i>,
        "<a href="#scopes" title="Scopes">Scopes</a>" : <i>[ String, ... ]</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#subjectmatchattribute" title="SubjectMatchAttribute">SubjectMatchAttribute</a>" : <i>String</i>,
        "<a href="#subjectmatchtype" title="SubjectMatchType">SubjectMatchType</a>" : <i>String</i>,
        "<a href="#suspendedaction" title="SuspendedAction">SuspendedAction</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#usernametemplate" title="UsernameTemplate">UsernameTemplate</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::SocialIdp
Properties:
    <a href="#accountlinkaction" title="AccountLinkAction">AccountLinkAction</a>: <i>String</i>
    <a href="#accountlinkgroupinclude" title="AccountLinkGroupInclude">AccountLinkGroupInclude</a>: <i>
      - String</i>
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#clientsecret" title="ClientSecret">ClientSecret</a>: <i>String</i>
    <a href="#deprovisionedaction" title="DeprovisionedAction">DeprovisionedAction</a>: <i>String</i>
    <a href="#groupsaction" title="GroupsAction">GroupsAction</a>: <i>String</i>
    <a href="#groupsassignment" title="GroupsAssignment">GroupsAssignment</a>: <i>
      - String</i>
    <a href="#groupsattribute" title="GroupsAttribute">GroupsAttribute</a>: <i>String</i>
    <a href="#groupsfilter" title="GroupsFilter">GroupsFilter</a>: <i>
      - String</i>
    <a href="#issuermode" title="IssuerMode">IssuerMode</a>: <i>String</i>
    <a href="#matchattribute" title="MatchAttribute">MatchAttribute</a>: <i>String</i>
    <a href="#matchtype" title="MatchType">MatchType</a>: <i>String</i>
    <a href="#maxclockskew" title="MaxClockSkew">MaxClockSkew</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#profilemaster" title="ProfileMaster">ProfileMaster</a>: <i>Boolean</i>
    <a href="#protocoltype" title="ProtocolType">ProtocolType</a>: <i>String</i>
    <a href="#provisioningaction" title="ProvisioningAction">ProvisioningAction</a>: <i>String</i>
    <a href="#requestsignaturealgorithm" title="RequestSignatureAlgorithm">RequestSignatureAlgorithm</a>: <i>String</i>
    <a href="#requestsignaturescope" title="RequestSignatureScope">RequestSignatureScope</a>: <i>String</i>
    <a href="#responsesignaturealgorithm" title="ResponseSignatureAlgorithm">ResponseSignatureAlgorithm</a>: <i>String</i>
    <a href="#responsesignaturescope" title="ResponseSignatureScope">ResponseSignatureScope</a>: <i>String</i>
    <a href="#scopes" title="Scopes">Scopes</a>: <i>
      - String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#subjectmatchattribute" title="SubjectMatchAttribute">SubjectMatchAttribute</a>: <i>String</i>
    <a href="#subjectmatchtype" title="SubjectMatchType">SubjectMatchType</a>: <i>String</i>
    <a href="#suspendedaction" title="SuspendedAction">SuspendedAction</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#usernametemplate" title="UsernameTemplate">UsernameTemplate</a>: <i>String</i>
</pre>

## Properties

#### AccountLinkAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountLinkGroupInclude

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeprovisionedAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsAssignment

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsFilter

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuerMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxClockSkew

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileMaster

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisioningAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestSignatureAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestSignatureScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseSignatureAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseSignatureScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scopes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectMatchAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectMatchType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuspendedAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernameTemplate

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

#### AuthorizationBinding

Returns the <code>AuthorizationBinding</code> value.

#### AuthorizationUrl

Returns the <code>AuthorizationUrl</code> value.

#### Id

Returns the <code>Id</code> value.

#### TokenBinding

Returns the <code>TokenBinding</code> value.

#### TokenUrl

Returns the <code>TokenUrl</code> value.

