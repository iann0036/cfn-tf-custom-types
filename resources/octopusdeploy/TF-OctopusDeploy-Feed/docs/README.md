# TF::OctopusDeploy::Feed

CloudFormation equivalent of octopusdeploy_feed

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OctopusDeploy::Feed",
    "Properties" : {
        "<a href="#accesskey" title="AccessKey">AccessKey</a>" : <i>String</i>,
        "<a href="#apiversion" title="ApiVersion">ApiVersion</a>" : <i>String</i>,
        "<a href="#deleteunreleasedpackagesafterdays" title="DeleteUnreleasedPackagesAfterDays">DeleteUnreleasedPackagesAfterDays</a>" : <i>Double</i>,
        "<a href="#downloadattempts" title="DownloadAttempts">DownloadAttempts</a>" : <i>Double</i>,
        "<a href="#downloadretrybackoffseconds" title="DownloadRetryBackoffSeconds">DownloadRetryBackoffSeconds</a>" : <i>Double</i>,
        "<a href="#feedtype" title="FeedType">FeedType</a>" : <i>String</i>,
        "<a href="#feeduri" title="FeedUri">FeedUri</a>" : <i>String</i>,
        "<a href="#isenhancedmode" title="IsEnhancedMode">IsEnhancedMode</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#packageacquisitionlocationoptions" title="PackageAcquisitionLocationOptions">PackageAcquisitionLocationOptions</a>" : <i>[ String, ... ]</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#registrypath" title="RegistryPath">RegistryPath</a>" : <i>String</i>,
        "<a href="#secretkey" title="SecretKey">SecretKey</a>" : <i>String</i>,
        "<a href="#spaceid" title="SpaceId">SpaceId</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OctopusDeploy::Feed
Properties:
    <a href="#accesskey" title="AccessKey">AccessKey</a>: <i>String</i>
    <a href="#apiversion" title="ApiVersion">ApiVersion</a>: <i>String</i>
    <a href="#deleteunreleasedpackagesafterdays" title="DeleteUnreleasedPackagesAfterDays">DeleteUnreleasedPackagesAfterDays</a>: <i>Double</i>
    <a href="#downloadattempts" title="DownloadAttempts">DownloadAttempts</a>: <i>Double</i>
    <a href="#downloadretrybackoffseconds" title="DownloadRetryBackoffSeconds">DownloadRetryBackoffSeconds</a>: <i>Double</i>
    <a href="#feedtype" title="FeedType">FeedType</a>: <i>String</i>
    <a href="#feeduri" title="FeedUri">FeedUri</a>: <i>String</i>
    <a href="#isenhancedmode" title="IsEnhancedMode">IsEnhancedMode</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#packageacquisitionlocationoptions" title="PackageAcquisitionLocationOptions">PackageAcquisitionLocationOptions</a>: <i>
      - String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#registrypath" title="RegistryPath">RegistryPath</a>: <i>String</i>
    <a href="#secretkey" title="SecretKey">SecretKey</a>: <i>String</i>
    <a href="#spaceid" title="SpaceId">SpaceId</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### AccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteUnreleasedPackagesAfterDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownloadAttempts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownloadRetryBackoffSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeedType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeedUri

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnhancedMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageAcquisitionLocationOptions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpaceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

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

#### Region

Returns the <code>Region</code> value.

