# TF::Panos::UrlFilteringSecurityProfile

Manages URL filtering security profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::UrlFilteringSecurityProfile",
    "Properties" : {
        "<a href="#alertcategories" title="AlertCategories">AlertCategories</a>" : <i>[ String, ... ]</i>,
        "<a href="#allowcategories" title="AllowCategories">AllowCategories</a>" : <i>[ String, ... ]</i>,
        "<a href="#allowlist" title="AllowList">AllowList</a>" : <i>[ String, ... ]</i>,
        "<a href="#blockcategories" title="BlockCategories">BlockCategories</a>" : <i>[ String, ... ]</i>,
        "<a href="#blocklist" title="BlockList">BlockList</a>" : <i>[ String, ... ]</i>,
        "<a href="#blocklistaction" title="BlockListAction">BlockListAction</a>" : <i>String</i>,
        "<a href="#continuecategories" title="ContinueCategories">ContinueCategories</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#dynamicurl" title="DynamicUrl">DynamicUrl</a>" : <i>Boolean</i>,
        "<a href="#expiredlicenseaction" title="ExpiredLicenseAction">ExpiredLicenseAction</a>" : <i>Boolean</i>,
        "<a href="#logcontainerpageonly" title="LogContainerPageOnly">LogContainerPageOnly</a>" : <i>Boolean</i>,
        "<a href="#loghttpheaderreferer" title="LogHttpHeaderReferer">LogHttpHeaderReferer</a>" : <i>Boolean</i>,
        "<a href="#loghttpheaderuseragent" title="LogHttpHeaderUserAgent">LogHttpHeaderUserAgent</a>" : <i>Boolean</i>,
        "<a href="#loghttpheaderxff" title="LogHttpHeaderXff">LogHttpHeaderXff</a>" : <i>Boolean</i>,
        "<a href="#machinelearningexceptions" title="MachineLearningExceptions">MachineLearningExceptions</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overridecategories" title="OverrideCategories">OverrideCategories</a>" : <i>[ String, ... ]</i>,
        "<a href="#safesearchenforcement" title="SafeSearchEnforcement">SafeSearchEnforcement</a>" : <i>Boolean</i>,
        "<a href="#trackcontainerpage" title="TrackContainerPage">TrackContainerPage</a>" : <i>Boolean</i>,
        "<a href="#ucdalertcategories" title="UcdAlertCategories">UcdAlertCategories</a>" : <i>[ String, ... ]</i>,
        "<a href="#ucdallowcategories" title="UcdAllowCategories">UcdAllowCategories</a>" : <i>[ String, ... ]</i>,
        "<a href="#ucdblockcategories" title="UcdBlockCategories">UcdBlockCategories</a>" : <i>[ String, ... ]</i>,
        "<a href="#ucdcontinuecategories" title="UcdContinueCategories">UcdContinueCategories</a>" : <i>[ String, ... ]</i>,
        "<a href="#ucdlogseverity" title="UcdLogSeverity">UcdLogSeverity</a>" : <i>String</i>,
        "<a href="#ucdmode" title="UcdMode">UcdMode</a>" : <i>String</i>,
        "<a href="#ucdmodegroupmapping" title="UcdModeGroupMapping">UcdModeGroupMapping</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#httpheaderinsertion" title="HttpHeaderInsertion">HttpHeaderInsertion</a>" : <i>[ <a href="httpheaderinsertiondefinition.md">HttpHeaderInsertionDefinition</a>, ... ]</i>,
        "<a href="#machinelearningmodel" title="MachineLearningModel">MachineLearningModel</a>" : <i>[ <a href="machinelearningmodeldefinition.md">MachineLearningModelDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::UrlFilteringSecurityProfile
Properties:
    <a href="#alertcategories" title="AlertCategories">AlertCategories</a>: <i>
      - String</i>
    <a href="#allowcategories" title="AllowCategories">AllowCategories</a>: <i>
      - String</i>
    <a href="#allowlist" title="AllowList">AllowList</a>: <i>
      - String</i>
    <a href="#blockcategories" title="BlockCategories">BlockCategories</a>: <i>
      - String</i>
    <a href="#blocklist" title="BlockList">BlockList</a>: <i>
      - String</i>
    <a href="#blocklistaction" title="BlockListAction">BlockListAction</a>: <i>String</i>
    <a href="#continuecategories" title="ContinueCategories">ContinueCategories</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#dynamicurl" title="DynamicUrl">DynamicUrl</a>: <i>Boolean</i>
    <a href="#expiredlicenseaction" title="ExpiredLicenseAction">ExpiredLicenseAction</a>: <i>Boolean</i>
    <a href="#logcontainerpageonly" title="LogContainerPageOnly">LogContainerPageOnly</a>: <i>Boolean</i>
    <a href="#loghttpheaderreferer" title="LogHttpHeaderReferer">LogHttpHeaderReferer</a>: <i>Boolean</i>
    <a href="#loghttpheaderuseragent" title="LogHttpHeaderUserAgent">LogHttpHeaderUserAgent</a>: <i>Boolean</i>
    <a href="#loghttpheaderxff" title="LogHttpHeaderXff">LogHttpHeaderXff</a>: <i>Boolean</i>
    <a href="#machinelearningexceptions" title="MachineLearningExceptions">MachineLearningExceptions</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overridecategories" title="OverrideCategories">OverrideCategories</a>: <i>
      - String</i>
    <a href="#safesearchenforcement" title="SafeSearchEnforcement">SafeSearchEnforcement</a>: <i>Boolean</i>
    <a href="#trackcontainerpage" title="TrackContainerPage">TrackContainerPage</a>: <i>Boolean</i>
    <a href="#ucdalertcategories" title="UcdAlertCategories">UcdAlertCategories</a>: <i>
      - String</i>
    <a href="#ucdallowcategories" title="UcdAllowCategories">UcdAllowCategories</a>: <i>
      - String</i>
    <a href="#ucdblockcategories" title="UcdBlockCategories">UcdBlockCategories</a>: <i>
      - String</i>
    <a href="#ucdcontinuecategories" title="UcdContinueCategories">UcdContinueCategories</a>: <i>
      - String</i>
    <a href="#ucdlogseverity" title="UcdLogSeverity">UcdLogSeverity</a>: <i>String</i>
    <a href="#ucdmode" title="UcdMode">UcdMode</a>: <i>String</i>
    <a href="#ucdmodegroupmapping" title="UcdModeGroupMapping">UcdModeGroupMapping</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#httpheaderinsertion" title="HttpHeaderInsertion">HttpHeaderInsertion</a>: <i>
      - <a href="httpheaderinsertiondefinition.md">HttpHeaderInsertionDefinition</a></i>
    <a href="#machinelearningmodel" title="MachineLearningModel">MachineLearningModel</a>: <i>
      - <a href="machinelearningmodeldefinition.md">MachineLearningModelDefinition</a></i>
</pre>

## Properties

#### AlertCategories

List of categories to alert.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowCategories

List of categories to allow.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowList

Allow list.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockCategories

List of categories to block.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockList

Block list.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockListAction

Block list action.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContinueCategories

List of categories to continue.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

The device group location (default: `shared`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicUrl

Dynamic URL.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpiredLicenseAction

Expired license action.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogContainerPageOnly

Log container page only.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogHttpHeaderReferer

HTTP header logging: Referer.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogHttpHeaderUserAgent

HTTP header logging: User-Agent.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogHttpHeaderXff

HTTP header logging: X-Forwarded-For.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineLearningExceptions

List of machine learning exceptions.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideCategories

List of categories to override.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SafeSearchEnforcement

Safe search enforcement.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrackContainerPage

Track the container page.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UcdAlertCategories

Categories alerted on with
user credential submission.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UcdAllowCategories

Categories allowed with user
credential submission.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UcdBlockCategories

Categories blocked with
user credential submission.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UcdContinueCategories

Categories continued with
user credential submission.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UcdLogSeverity

User credential
detection: valid username detected log severity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UcdMode

User credential detection mode.  Valid values are
`disabled` (default), `ip-user`, `domain-credentials`, or `group-mapping`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UcdModeGroupMapping

User
credential detection: the group mapping settings.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The vsys location (default: `vsys1`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeaderInsertion

_Required_: No

_Type_: List of <a href="httpheaderinsertiondefinition.md">HttpHeaderInsertionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineLearningModel

_Required_: No

_Type_: List of <a href="machinelearningmodeldefinition.md">MachineLearningModelDefinition</a>

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

