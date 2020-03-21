# Terraform::AzureRM::CdnEndpoint

CloudFormation equivalent of azurerm_cdn_endpoint

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::CdnEndpoint",
    "Properties" : {
        "<a href="#contenttypestocompress" title="ContentTypesToCompress">ContentTypesToCompress</a>" : <i>[ String, ... ]</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
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

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

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
