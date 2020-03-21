# Terraform::CloudScale::Server

CloudFormation equivalent of cloudscale_server

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::CloudScale::Server",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#allowstoppingforupdate" title="AllowStoppingForUpdate">AllowStoppingForUpdate</a>" : <i>Boolean</i>,
        "<a href="#bulkvolumesizegb" title="BulkVolumeSizeGb">BulkVolumeSizeGb</a>" : <i>Double</i>,
        "<a href="#flavorslug" title="FlavorSlug">FlavorSlug</a>" : <i>String</i>,
        "<a href="#href" title="Href">Href</a>" : <i>String</i>,
        "<a href="#imageslug" title="ImageSlug">ImageSlug</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#privateipv4address" title="PrivateIpv4Address">PrivateIpv4Address</a>" : <i>String</i>,
        "<a href="#publicipv4address" title="PublicIpv4Address">PublicIpv4Address</a>" : <i>String</i>,
        "<a href="#publicipv6address" title="PublicIpv6Address">PublicIpv6Address</a>" : <i>String</i>,
        "<a href="#servergroupids" title="ServerGroupIds">ServerGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#servergroups" title="ServerGroups">ServerGroups</a>" : <i>[ &lt;a href=&#34;servergroups.md&#34;&gt;ServerGroups&lt;/a&gt;, ... ]</i>,
        "<a href="#sshfingerprints" title="SshFingerprints">SshFingerprints</a>" : <i>[ String, ... ]</i>,
        "<a href="#sshhostkeys" title="SshHostKeys">SshHostKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#useipv6" title="UseIpv6">UseIpv6</a>" : <i>Boolean</i>,
        "<a href="#useprivatenetwork" title="UsePrivateNetwork">UsePrivateNetwork</a>" : <i>Boolean</i>,
        "<a href="#usepublicnetwork" title="UsePublicNetwork">UsePublicNetwork</a>" : <i>Boolean</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#volumesizegb" title="VolumeSizeGb">VolumeSizeGb</a>" : <i>Double</i>,
        "<a href="#volumes" title="Volumes">Volumes</a>" : <i>[ &lt;a href=&#34;volumes.md&#34;&gt;Volumes&lt;/a&gt;, ... ]</i>,
        "<a href="#zoneslug" title="ZoneSlug">ZoneSlug</a>" : <i>String</i>,
        "<a href="#interfaces" title="Interfaces">Interfaces</a>" : <i>[ &lt;a href=&#34;interfaces.md&#34;&gt;Interfaces&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::CloudScale::Server
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#allowstoppingforupdate" title="AllowStoppingForUpdate">AllowStoppingForUpdate</a>: <i>Boolean</i>
    <a href="#bulkvolumesizegb" title="BulkVolumeSizeGb">BulkVolumeSizeGb</a>: <i>Double</i>
    <a href="#flavorslug" title="FlavorSlug">FlavorSlug</a>: <i>String</i>
    <a href="#href" title="Href">Href</a>: <i>String</i>
    <a href="#imageslug" title="ImageSlug">ImageSlug</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#privateipv4address" title="PrivateIpv4Address">PrivateIpv4Address</a>: <i>String</i>
    <a href="#publicipv4address" title="PublicIpv4Address">PublicIpv4Address</a>: <i>String</i>
    <a href="#publicipv6address" title="PublicIpv6Address">PublicIpv6Address</a>: <i>String</i>
    <a href="#servergroupids" title="ServerGroupIds">ServerGroupIds</a>: <i>
      - String</i>
    <a href="#servergroups" title="ServerGroups">ServerGroups</a>: <i>
      - &lt;a href=&#34;servergroups.md&#34;&gt;ServerGroups&lt;/a&gt;</i>
    <a href="#sshfingerprints" title="SshFingerprints">SshFingerprints</a>: <i>
      - String</i>
    <a href="#sshhostkeys" title="SshHostKeys">SshHostKeys</a>: <i>
      - String</i>
    <a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#useipv6" title="UseIpv6">UseIpv6</a>: <i>Boolean</i>
    <a href="#useprivatenetwork" title="UsePrivateNetwork">UsePrivateNetwork</a>: <i>Boolean</i>
    <a href="#usepublicnetwork" title="UsePublicNetwork">UsePublicNetwork</a>: <i>Boolean</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#volumesizegb" title="VolumeSizeGb">VolumeSizeGb</a>: <i>Double</i>
    <a href="#volumes" title="Volumes">Volumes</a>: <i>
      - &lt;a href=&#34;volumes.md&#34;&gt;Volumes&lt;/a&gt;</i>
    <a href="#zoneslug" title="ZoneSlug">ZoneSlug</a>: <i>String</i>
    <a href="#interfaces" title="Interfaces">Interfaces</a>: <i>
      - &lt;a href=&#34;interfaces.md&#34;&gt;Interfaces&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowStoppingForUpdate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BulkVolumeSizeGb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlavorSlug

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Href

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageSlug

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpv4Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpv4Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpv6Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerGroups

_Required_: No

_Type_: List of &lt;a href=&#34;servergroups.md&#34;&gt;ServerGroups&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshFingerprints

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshHostKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseIpv6

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsePrivateNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsePublicNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeSizeGb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volumes

_Required_: No

_Type_: List of &lt;a href=&#34;volumes.md&#34;&gt;Volumes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneSlug

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interfaces

_Required_: No

_Type_: List of &lt;a href=&#34;interfaces.md&#34;&gt;Interfaces&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Href

Returns the &lt;code&gt;Href&lt;/code&gt; value.

#### PrivateIpv4Address

Returns the &lt;code&gt;PrivateIpv4Address&lt;/code&gt; value.

#### PublicIpv4Address

Returns the &lt;code&gt;PublicIpv4Address&lt;/code&gt; value.

#### PublicIpv6Address

Returns the &lt;code&gt;PublicIpv6Address&lt;/code&gt; value.

#### ServerGroups

Returns the &lt;code&gt;ServerGroups&lt;/code&gt; value.

#### SshFingerprints

Returns the &lt;code&gt;SshFingerprints&lt;/code&gt; value.

#### SshHostKeys

Returns the &lt;code&gt;SshHostKeys&lt;/code&gt; value.

#### Volumes

Returns the &lt;code&gt;Volumes&lt;/code&gt; value.

