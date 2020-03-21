# Terraform::AzureRM::CdnEndpoint

A CDN Endpoint is the entity within a CDN Profile containing configuration information regarding caching behaviors and origins. The CDN Endpoint is exposed using the URL format <endpointname>.azureedge.net.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::CdnEndpoint",
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
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#geofilter" title="GeoFilter">GeoFilter</a>" : <i>[ <a href="geofilter.md">GeoFilter</a>, ... ]</i>,
        "<a href="#origin" title="Origin">Origin</a>" : <i>[ <a href="origin.md">Origin</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::CdnEndpoint
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
      - <a href="tags.md">Tags</a></i>
    <a href="#geofilter" title="GeoFilter">GeoFilter</a>: <i>
      - <a href="geofilter.md">GeoFilter</a></i>
    <a href="#origin" title="Origin">Origin</a>: <i>
      - <a href="origin.md">Origin</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ContentTypesToCompress

An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCompressionEnabled

Indicates whether compression is to be enabled. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHttpAllowed

Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHttpsAllowed

Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the CDN Endpoint. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptimizationType

What types of optimization should this CDN Endpoint optimize for? Possible values include `DynamicSiteAcceleration`, `GeneralMediaStreaming`, `GeneralWebDelivery`, `LargeFileDownload` and `VideoOnDemandMediaStreaming`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginHostHeader

The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginPath

The path used at for origin requests.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProbePath

the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the `origin_path`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileName

The CDN Profile to which to attach the CDN Endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuerystringCachingBehaviour

Sets query string caching behavior. Allowed values are `IgnoreQueryString`, `BypassCaching` and `UseQueryString`. Defaults to `IgnoreQueryString`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the CDN Endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoFilter

_Required_: No

_Type_: List of <a href="geofilter.md">GeoFilter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

_Required_: No

_Type_: List of <a href="origin.md">Origin</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

