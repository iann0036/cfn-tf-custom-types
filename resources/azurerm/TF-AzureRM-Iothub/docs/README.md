# TF::AzureRM::Iothub

Manages an IotHub

~> **NOTE:** Endpoints can be defined either directly on the `azurerm_iothub` resource, or using the `azurerm_iothub_endpoint_*` resources - but the two ways of defining the endpoints cannot be used together. If both are used against the same IoTHub, spurious changes will occur. Also, defining a `azurerm_iothub_endpoint_*` resource and another endpoint of a different type directly on the `azurerm_iothub` resource is not supported.

~> **NOTE:** Routes can be defined either directly on the `azurerm_iothub` resource, or using the `azurerm_iothub_route` resource - but the two cannot be used together. If both are used against the same IoTHub, spurious changes will occur.

~> **NOTE:** Enrichments can be defined either directly on the `azurerm_iothub` resource, or using the `azurerm_iothub_enrichment` resource - but the two cannot be used together. If both are used against the same IoTHub, spurious changes will occur.

~> **NOTE:** Fallback route can be defined either directly on the `azurer...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::Iothub",
    "Properties" : {
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>[ <a href="endpointdefinition.md">EndpointDefinition</a>, ... ]</i>,
        "<a href="#enrichment" title="Enrichment">Enrichment</a>" : <i>[ <a href="enrichmentdefinition.md">EnrichmentDefinition</a>, ... ]</i>,
        "<a href="#eventhubpartitioncount" title="EventHubPartitionCount">EventHubPartitionCount</a>" : <i>Double</i>,
        "<a href="#eventhubretentionindays" title="EventHubRetentionInDays">EventHubRetentionInDays</a>" : <i>Double</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#publicnetworkaccessenabled" title="PublicNetworkAccessEnabled">PublicNetworkAccessEnabled</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#route" title="Route">Route</a>" : <i>[ <a href="routedefinition.md">RouteDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#fallbackroute" title="FallbackRoute">FallbackRoute</a>" : <i>[ <a href="fallbackroutedefinition.md">FallbackRouteDefinition</a>, ... ]</i>,
        "<a href="#fileupload" title="FileUpload">FileUpload</a>" : <i>[ <a href="fileuploaddefinition.md">FileUploadDefinition</a>, ... ]</i>,
        "<a href="#ipfilterrule" title="IpFilterRule">IpFilterRule</a>" : <i>[ <a href="ipfilterruledefinition.md">IpFilterRuleDefinition</a>, ... ]</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>[ <a href="skudefinition.md">SkuDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::Iothub
Properties:
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>
      - <a href="endpointdefinition.md">EndpointDefinition</a></i>
    <a href="#enrichment" title="Enrichment">Enrichment</a>: <i>
      - <a href="enrichmentdefinition.md">EnrichmentDefinition</a></i>
    <a href="#eventhubpartitioncount" title="EventHubPartitionCount">EventHubPartitionCount</a>: <i>Double</i>
    <a href="#eventhubretentionindays" title="EventHubRetentionInDays">EventHubRetentionInDays</a>: <i>Double</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#publicnetworkaccessenabled" title="PublicNetworkAccessEnabled">PublicNetworkAccessEnabled</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#route" title="Route">Route</a>: <i>
      - <a href="routedefinition.md">RouteDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#fallbackroute" title="FallbackRoute">FallbackRoute</a>: <i>
      - <a href="fallbackroutedefinition.md">FallbackRouteDefinition</a></i>
    <a href="#fileupload" title="FileUpload">FileUpload</a>: <i>
      - <a href="fileuploaddefinition.md">FileUploadDefinition</a></i>
    <a href="#ipfilterrule" title="IpFilterRule">IpFilterRule</a>: <i>
      - <a href="ipfilterruledefinition.md">IpFilterRuleDefinition</a></i>
    <a href="#sku" title="Sku">Sku</a>: <i>
      - <a href="skudefinition.md">SkuDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Endpoint

An `endpoint` block as defined below.

_Required_: No

_Type_: List of <a href="endpointdefinition.md">EndpointDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enrichment

A `enrichment` block as defined below.

_Required_: No

_Type_: List of <a href="enrichmentdefinition.md">EnrichmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventHubPartitionCount

The number of device-to-cloud partitions used by backing event hubs. Must be between `2` and `128`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventHubRetentionInDays

The event hub retention to use in days. Must be between `1` and `7`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource has to be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTlsVersion

Specifies the minimum TLS version to support for this hub. The only valid value is `1.2`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the IotHub resource. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicNetworkAccessEnabled

Is the IotHub resource accessible from a public network?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Route

A `route` block as defined below.

_Required_: No

_Type_: List of <a href="routedefinition.md">RouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackRoute

_Required_: No

_Type_: List of <a href="fallbackroutedefinition.md">FallbackRouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileUpload

_Required_: No

_Type_: List of <a href="fileuploaddefinition.md">FileUploadDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpFilterRule

_Required_: No

_Type_: List of <a href="ipfilterruledefinition.md">IpFilterRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

_Required_: No

_Type_: List of <a href="skudefinition.md">SkuDefinition</a>

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

#### EventHubEventsEndpoint

Returns the <code>EventHubEventsEndpoint</code> value.

#### EventHubEventsPath

Returns the <code>EventHubEventsPath</code> value.

#### EventHubOperationsEndpoint

Returns the <code>EventHubOperationsEndpoint</code> value.

#### EventHubOperationsPath

Returns the <code>EventHubOperationsPath</code> value.

#### Hostname

Returns the <code>Hostname</code> value.

#### Id

Returns the <code>Id</code> value.

#### SharedAccessPolicy

Returns the <code>SharedAccessPolicy</code> value.

#### Type

Returns the <code>Type</code> value.

