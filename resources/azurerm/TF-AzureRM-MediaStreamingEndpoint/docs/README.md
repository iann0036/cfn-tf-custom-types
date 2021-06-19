# TF::AzureRM::MediaStreamingEndpoint

Manages a Streaming Endpoint.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::MediaStreamingEndpoint",
    "Properties" : {
        "<a href="#autostartenabled" title="AutoStartEnabled">AutoStartEnabled</a>" : <i>Boolean</i>,
        "<a href="#cdnenabled" title="CdnEnabled">CdnEnabled</a>" : <i>Boolean</i>,
        "<a href="#cdnprofile" title="CdnProfile">CdnProfile</a>" : <i>String</i>,
        "<a href="#cdnprovider" title="CdnProvider">CdnProvider</a>" : <i>String</i>,
        "<a href="#customhostnames" title="CustomHostNames">CustomHostNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#maxcacheageseconds" title="MaxCacheAgeSeconds">MaxCacheAgeSeconds</a>" : <i>Double</i>,
        "<a href="#mediaservicesaccountname" title="MediaServicesAccountName">MediaServicesAccountName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#scaleunits" title="ScaleUnits">ScaleUnits</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#accesscontrol" title="AccessControl">AccessControl</a>" : <i>[ <a href="accesscontroldefinition.md">AccessControlDefinition</a>, ... ]</i>,
        "<a href="#crosssiteaccesspolicy" title="CrossSiteAccessPolicy">CrossSiteAccessPolicy</a>" : <i>[ <a href="crosssiteaccesspolicydefinition.md">CrossSiteAccessPolicyDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::MediaStreamingEndpoint
Properties:
    <a href="#autostartenabled" title="AutoStartEnabled">AutoStartEnabled</a>: <i>Boolean</i>
    <a href="#cdnenabled" title="CdnEnabled">CdnEnabled</a>: <i>Boolean</i>
    <a href="#cdnprofile" title="CdnProfile">CdnProfile</a>: <i>String</i>
    <a href="#cdnprovider" title="CdnProvider">CdnProvider</a>: <i>String</i>
    <a href="#customhostnames" title="CustomHostNames">CustomHostNames</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#maxcacheageseconds" title="MaxCacheAgeSeconds">MaxCacheAgeSeconds</a>: <i>Double</i>
    <a href="#mediaservicesaccountname" title="MediaServicesAccountName">MediaServicesAccountName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#scaleunits" title="ScaleUnits">ScaleUnits</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#accesscontrol" title="AccessControl">AccessControl</a>: <i>
      - <a href="accesscontroldefinition.md">AccessControlDefinition</a></i>
    <a href="#crosssiteaccesspolicy" title="CrossSiteAccessPolicy">CrossSiteAccessPolicy</a>: <i>
      - <a href="crosssiteaccesspolicydefinition.md">CrossSiteAccessPolicyDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AutoStartEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdnEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdnProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdnProvider

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHostNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCacheAgeSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MediaServicesAccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleUnits

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessControl

_Required_: No

_Type_: List of <a href="accesscontroldefinition.md">AccessControlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrossSiteAccessPolicy

_Required_: No

_Type_: List of <a href="crosssiteaccesspolicydefinition.md">CrossSiteAccessPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### HostName

Returns the <code>HostName</code> value.

#### Id

Returns the <code>Id</code> value.

