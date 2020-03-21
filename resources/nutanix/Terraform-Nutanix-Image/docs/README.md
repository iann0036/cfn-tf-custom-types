# Terraform::Nutanix::Image

CloudFormation equivalent of nutanix_image

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Nutanix::Image",
    "Properties" : {
        "<a href="#architecture" title="Architecture">Architecture</a>" : <i>String</i>,
        "<a href="#availabilityzonereference" title="AvailabilityZoneReference">AvailabilityZoneReference</a>" : <i>[ &lt;a href=&#34;availabilityzonereference.md&#34;&gt;AvailabilityZoneReference&lt;/a&gt;, ... ]</i>,
        "<a href="#checksum" title="Checksum">Checksum</a>" : <i>[ &lt;a href=&#34;checksum.md&#34;&gt;Checksum&lt;/a&gt;, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#imagetype" title="ImageType">ImageType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ownerreference" title="OwnerReference">OwnerReference</a>" : <i>[ &lt;a href=&#34;ownerreference.md&#34;&gt;OwnerReference&lt;/a&gt;, ... ]</i>,
        "<a href="#projectreference" title="ProjectReference">ProjectReference</a>" : <i>[ &lt;a href=&#34;projectreference.md&#34;&gt;ProjectReference&lt;/a&gt;, ... ]</i>,
        "<a href="#sourcepath" title="SourcePath">SourcePath</a>" : <i>String</i>,
        "<a href="#sourceuri" title="SourceUri">SourceUri</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>[ &lt;a href=&#34;version.md&#34;&gt;Version&lt;/a&gt;, ... ]</i>,
        "<a href="#categories" title="Categories">Categories</a>" : <i>[ &lt;a href=&#34;categories.md&#34;&gt;Categories&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Nutanix::Image
Properties:
    <a href="#architecture" title="Architecture">Architecture</a>: <i>String</i>
    <a href="#availabilityzonereference" title="AvailabilityZoneReference">AvailabilityZoneReference</a>: <i>
      - &lt;a href=&#34;availabilityzonereference.md&#34;&gt;AvailabilityZoneReference&lt;/a&gt;</i>
    <a href="#checksum" title="Checksum">Checksum</a>: <i>
      - &lt;a href=&#34;checksum.md&#34;&gt;Checksum&lt;/a&gt;</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#imagetype" title="ImageType">ImageType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ownerreference" title="OwnerReference">OwnerReference</a>: <i>
      - &lt;a href=&#34;ownerreference.md&#34;&gt;OwnerReference&lt;/a&gt;</i>
    <a href="#projectreference" title="ProjectReference">ProjectReference</a>: <i>
      - &lt;a href=&#34;projectreference.md&#34;&gt;ProjectReference&lt;/a&gt;</i>
    <a href="#sourcepath" title="SourcePath">SourcePath</a>: <i>String</i>
    <a href="#sourceuri" title="SourceUri">SourceUri</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>
      - &lt;a href=&#34;version.md&#34;&gt;Version&lt;/a&gt;</i>
    <a href="#categories" title="Categories">Categories</a>: <i>
      - &lt;a href=&#34;categories.md&#34;&gt;Categories&lt;/a&gt;</i>
</pre>

## Properties

#### Architecture

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZoneReference

_Required_: No

_Type_: List of &lt;a href=&#34;availabilityzonereference.md&#34;&gt;AvailabilityZoneReference&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Checksum

_Required_: No

_Type_: List of &lt;a href=&#34;checksum.md&#34;&gt;Checksum&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerReference

_Required_: No

_Type_: List of &lt;a href=&#34;ownerreference.md&#34;&gt;OwnerReference&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectReference

_Required_: No

_Type_: List of &lt;a href=&#34;projectreference.md&#34;&gt;ProjectReference&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: List of &lt;a href=&#34;version.md&#34;&gt;Version&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: No

_Type_: List of &lt;a href=&#34;categories.md&#34;&gt;Categories&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiVersion

Returns the &lt;code&gt;ApiVersion&lt;/code&gt; value.

#### ClusterName

Returns the &lt;code&gt;ClusterName&lt;/code&gt; value.

#### ClusterUuid

Returns the &lt;code&gt;ClusterUuid&lt;/code&gt; value.

#### Metadata

Returns the &lt;code&gt;Metadata&lt;/code&gt; value.

#### RetrievalUriList

Returns the &lt;code&gt;RetrievalUriList&lt;/code&gt; value.

#### SizeBytes

Returns the &lt;code&gt;SizeBytes&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

