# TF::AzureRM::CdnEndpoint

A CDN Endpoint is the entity within a CDN Profile containing configuration information regarding caching behaviours and origins. The CDN Endpoint is exposed using the URL format <endpointname>.azureedge.net.

!> **Be Aware:** Azure is rolling out a breaking change on Friday 9th April which may cause issues with the CDN/FrontDoor resources. [More information is available in this Github issue](https://github.com/terraform-providers/terraform-provider-azurerm/issues/11231) - however unfortunately this may necessitate a breaking change to the CDN and FrontDoor resources, more information will be posted [in the Github issue](https://github.com/terraform-providers/terraform-provider-azurerm/issues/11231) as the necessary changes are identified.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::CdnEndpoint",
    "Properties" : {
        "<a href="#contenttypestocompress" title="ContentTypesToCompress">ContentTypesToCompress</a>" : <i>[ String, ... ]</i>,
        "<a href="#iscompressionenabled" title="IsCompressionEnabled">IsCompressionEnabled</a>" : <i>Boolean</i>,
        "<a href="#ishttpallowed" title="IsHttpAllowed">IsHttpAllowed</a>" : <i>Boolean</i>,
        "<a href="#ishttpsallowed" title="IsHttpsAllowed">IsHttpsAllowed</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#optimizationtype" title="OptimizationType">OptimizationType</a>" : <i>String</i>,
        "<a href="#originhostheader" title="OriginHostHeader">OriginHostHeader</a>" : <i>String</i>,
        "<a href="#originpath" title="OriginPath">OriginPath</a>" : <i>String</i>,
        "<a href="#probepath" title="ProbePath">ProbePath</a>" : <i>String</i>,
        "<a href="#profilename" title="ProfileName">ProfileName</a>" : <i>String</i>,
        "<a href="#querystringcachingbehaviour" title="QuerystringCachingBehaviour">QuerystringCachingBehaviour</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#deliveryrule" title="DeliveryRule">DeliveryRule</a>" : <i>[ <a href="deliveryruledefinition.md">DeliveryRuleDefinition</a>, ... ]</i>,
        "<a href="#geofilter" title="GeoFilter">GeoFilter</a>" : <i>[ <a href="geofilterdefinition.md">GeoFilterDefinition</a>, ... ]</i>,
        "<a href="#globaldeliveryrule" title="GlobalDeliveryRule">GlobalDeliveryRule</a>" : <i>[ <a href="globaldeliveryruledefinition.md">GlobalDeliveryRuleDefinition</a>, ... ]</i>,
        "<a href="#origin" title="Origin">Origin</a>" : <i>[ <a href="origindefinition.md">OriginDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::CdnEndpoint
Properties:
    <a href="#contenttypestocompress" title="ContentTypesToCompress">ContentTypesToCompress</a>: <i>
      - String</i>
    <a href="#iscompressionenabled" title="IsCompressionEnabled">IsCompressionEnabled</a>: <i>Boolean</i>
    <a href="#ishttpallowed" title="IsHttpAllowed">IsHttpAllowed</a>: <i>Boolean</i>
    <a href="#ishttpsallowed" title="IsHttpsAllowed">IsHttpsAllowed</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#optimizationtype" title="OptimizationType">OptimizationType</a>: <i>String</i>
    <a href="#originhostheader" title="OriginHostHeader">OriginHostHeader</a>: <i>String</i>
    <a href="#originpath" title="OriginPath">OriginPath</a>: <i>String</i>
    <a href="#probepath" title="ProbePath">ProbePath</a>: <i>String</i>
    <a href="#profilename" title="ProfileName">ProfileName</a>: <i>String</i>
    <a href="#querystringcachingbehaviour" title="QuerystringCachingBehaviour">QuerystringCachingBehaviour</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#deliveryrule" title="DeliveryRule">DeliveryRule</a>: <i>
      - <a href="deliveryruledefinition.md">DeliveryRuleDefinition</a></i>
    <a href="#geofilter" title="GeoFilter">GeoFilter</a>: <i>
      - <a href="geofilterdefinition.md">GeoFilterDefinition</a></i>
    <a href="#globaldeliveryrule" title="GlobalDeliveryRule">GlobalDeliveryRule</a>: <i>
      - <a href="globaldeliveryruledefinition.md">GlobalDeliveryRuleDefinition</a></i>
    <a href="#origin" title="Origin">Origin</a>: <i>
      - <a href="origindefinition.md">OriginDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ContentTypesToCompress

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCompressionEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHttpAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHttpsAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptimizationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginHostHeader

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProbePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuerystringCachingBehaviour

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryRule

_Required_: No

_Type_: List of <a href="deliveryruledefinition.md">DeliveryRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoFilter

_Required_: No

_Type_: List of <a href="geofilterdefinition.md">GeoFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalDeliveryRule

_Required_: No

_Type_: List of <a href="globaldeliveryruledefinition.md">GlobalDeliveryRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

_Required_: No

_Type_: List of <a href="origindefinition.md">OriginDefinition</a>

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

