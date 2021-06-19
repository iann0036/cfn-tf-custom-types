# TF::Alicloud::EciImageCache

An ECI Image Cache can help user to solve the time-consuming problem of image pull. For information about Alicloud ECI Image Cache and how to use it, see [What is Resource Alicloud ECI Image Cache](https://www.alibabacloud.com/help/doc-detail/146891.htm).

-> **NOTE:** Available in v1.89.0+.

-> **NOTE:** Each image cache corresponds to a snapshot, and the user does not delete the snapshot directly, otherwise the cache will fail.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::EciImageCache",
    "Properties" : {
        "<a href="#eipinstanceid" title="EipInstanceId">EipInstanceId</a>" : <i>String</i>,
        "<a href="#imagecachename" title="ImageCacheName">ImageCacheName</a>" : <i>String</i>,
        "<a href="#imagecachesize" title="ImageCacheSize">ImageCacheSize</a>" : <i>Double</i>,
        "<a href="#images" title="Images">Images</a>" : <i>[ String, ... ]</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#retentiondays" title="RetentionDays">RetentionDays</a>" : <i>Double</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#imageregistrycredential" title="ImageRegistryCredential">ImageRegistryCredential</a>" : <i>[ <a href="imageregistrycredentialdefinition.md">ImageRegistryCredentialDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::EciImageCache
Properties:
    <a href="#eipinstanceid" title="EipInstanceId">EipInstanceId</a>: <i>String</i>
    <a href="#imagecachename" title="ImageCacheName">ImageCacheName</a>: <i>String</i>
    <a href="#imagecachesize" title="ImageCacheSize">ImageCacheSize</a>: <i>Double</i>
    <a href="#images" title="Images">Images</a>: <i>
      - String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#retentiondays" title="RetentionDays">RetentionDays</a>: <i>Double</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#imageregistrycredential" title="ImageRegistryCredential">ImageRegistryCredential</a>: <i>
      - <a href="imageregistrycredentialdefinition.md">ImageRegistryCredentialDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### EipInstanceId

The instance ID of the Elastic IP Address (EIP). If you want to pull images from the Internet, you must specify an EIP to make sure that the container group can access the Internet. You can also configure the network address translation (NAT) gateway. We recommend that you configure the NAT gateway for the Internet access. Refer to [Public Network Access Method](https://help.aliyun.com/document_detail/99146.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageCacheName

The name of the image cache.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageCacheSize

The size of the image cache. Default to `20`. Unit: GiB.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Images

The images to be cached. The image name must be versioned.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The ID of the resource group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionDays

The retention days of the image cache. Once the image cache expires, it will be cleared. By default, the image cache never expires. Note: The image cache that fails to be created is retained for only one day.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

The ID of the security group. You do not need to specify the same security group as the container group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

The ID of the VSwitch. You do not need to specify the same VSwitch as the container group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The zone id to cache image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageRegistryCredential

_Required_: No

_Type_: List of <a href="imageregistrycredentialdefinition.md">ImageRegistryCredentialDefinition</a>

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

#### ContainerGroupId

Returns the <code>ContainerGroupId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

