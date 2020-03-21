# Terraform::AzureRM::StorageAccount

CloudFormation equivalent of azurerm_storage_account

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::StorageAccount",
    "Properties" : {
        "<a href="#accesstier" title="AccessTier">AccessTier</a>" : <i>String</i>,
        "<a href="#accountkind" title="AccountKind">AccountKind</a>" : <i>String</i>,
        "<a href="#accountreplicationtype" title="AccountReplicationType">AccountReplicationType</a>" : <i>String</i>,
        "<a href="#accounttier" title="AccountTier">AccountTier</a>" : <i>String</i>,
        "<a href="#enablehttpstrafficonly" title="EnableHttpsTrafficOnly">EnableHttpsTrafficOnly</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#ishnsenabled" title="IsHnsEnabled">IsHnsEnabled</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#blobproperties" title="BlobProperties">BlobProperties</a>" : <i>[ &lt;a href=&#34;blobproperties.md&#34;&gt;BlobProperties&lt;/a&gt;, ... ]</i>,
        "<a href="#customdomain" title="CustomDomain">CustomDomain</a>" : <i>[ &lt;a href=&#34;customdomain.md&#34;&gt;CustomDomain&lt;/a&gt;, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;, ... ]</i>,
        "<a href="#networkrules" title="NetworkRules">NetworkRules</a>" : <i>[ &lt;a href=&#34;networkrules.md&#34;&gt;NetworkRules&lt;/a&gt;, ... ]</i>,
        "<a href="#queueproperties" title="QueueProperties">QueueProperties</a>" : <i>[ &lt;a href=&#34;queueproperties.md&#34;&gt;QueueProperties&lt;/a&gt;, ... ]</i>,
        "<a href="#staticwebsite" title="StaticWebsite">StaticWebsite</a>" : <i>[ &lt;a href=&#34;staticwebsite.md&#34;&gt;StaticWebsite&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ &lt;a href=&#34;corsrule.md&#34;&gt;CorsRule&lt;/a&gt;, ... ]</i>,
        "<a href="#deleteretentionpolicy" title="DeleteRetentionPolicy">DeleteRetentionPolicy</a>" : <i>[ &lt;a href=&#34;deleteretentionpolicy.md&#34;&gt;DeleteRetentionPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#hourmetrics" title="HourMetrics">HourMetrics</a>" : <i>[ &lt;a href=&#34;hourmetrics.md&#34;&gt;HourMetrics&lt;/a&gt;, ... ]</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>[ &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;, ... ]</i>,
        "<a href="#minutemetrics" title="MinuteMetrics">MinuteMetrics</a>" : <i>[ &lt;a href=&#34;minutemetrics.md&#34;&gt;MinuteMetrics&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::StorageAccount
Properties:
    <a href="#accesstier" title="AccessTier">AccessTier</a>: <i>String</i>
    <a href="#accountkind" title="AccountKind">AccountKind</a>: <i>String</i>
    <a href="#accountreplicationtype" title="AccountReplicationType">AccountReplicationType</a>: <i>String</i>
    <a href="#accounttier" title="AccountTier">AccountTier</a>: <i>String</i>
    <a href="#enablehttpstrafficonly" title="EnableHttpsTrafficOnly">EnableHttpsTrafficOnly</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#ishnsenabled" title="IsHnsEnabled">IsHnsEnabled</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#blobproperties" title="BlobProperties">BlobProperties</a>: <i>
      - &lt;a href=&#34;blobproperties.md&#34;&gt;BlobProperties&lt;/a&gt;</i>
    <a href="#customdomain" title="CustomDomain">CustomDomain</a>: <i>
      - &lt;a href=&#34;customdomain.md&#34;&gt;CustomDomain&lt;/a&gt;</i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;</i>
    <a href="#networkrules" title="NetworkRules">NetworkRules</a>: <i>
      - &lt;a href=&#34;networkrules.md&#34;&gt;NetworkRules&lt;/a&gt;</i>
    <a href="#queueproperties" title="QueueProperties">QueueProperties</a>: <i>
      - &lt;a href=&#34;queueproperties.md&#34;&gt;QueueProperties&lt;/a&gt;</i>
    <a href="#staticwebsite" title="StaticWebsite">StaticWebsite</a>: <i>
      - &lt;a href=&#34;staticwebsite.md&#34;&gt;StaticWebsite&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - &lt;a href=&#34;corsrule.md&#34;&gt;CorsRule&lt;/a&gt;</i>
    <a href="#deleteretentionpolicy" title="DeleteRetentionPolicy">DeleteRetentionPolicy</a>: <i>
      - &lt;a href=&#34;deleteretentionpolicy.md&#34;&gt;DeleteRetentionPolicy&lt;/a&gt;</i>
    <a href="#hourmetrics" title="HourMetrics">HourMetrics</a>: <i>
      - &lt;a href=&#34;hourmetrics.md&#34;&gt;HourMetrics&lt;/a&gt;</i>
    <a href="#logging" title="Logging">Logging</a>: <i>
      - &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;</i>
    <a href="#minutemetrics" title="MinuteMetrics">MinuteMetrics</a>: <i>
      - &lt;a href=&#34;minutemetrics.md&#34;&gt;MinuteMetrics&lt;/a&gt;</i>
</pre>

## Properties

#### AccessTier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountKind

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountReplicationType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountTier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHttpsTrafficOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHnsEnabled

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

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlobProperties

_Required_: No

_Type_: List of &lt;a href=&#34;blobproperties.md&#34;&gt;BlobProperties&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomDomain

_Required_: No

_Type_: List of &lt;a href=&#34;customdomain.md&#34;&gt;CustomDomain&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkRules

_Required_: No

_Type_: List of &lt;a href=&#34;networkrules.md&#34;&gt;NetworkRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueProperties

_Required_: No

_Type_: List of &lt;a href=&#34;queueproperties.md&#34;&gt;QueueProperties&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticWebsite

_Required_: No

_Type_: List of &lt;a href=&#34;staticwebsite.md&#34;&gt;StaticWebsite&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsRule

_Required_: No

_Type_: List of &lt;a href=&#34;corsrule.md&#34;&gt;CorsRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteRetentionPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;deleteretentionpolicy.md&#34;&gt;DeleteRetentionPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourMetrics

_Required_: No

_Type_: List of &lt;a href=&#34;hourmetrics.md&#34;&gt;HourMetrics&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinuteMetrics

_Required_: No

_Type_: List of &lt;a href=&#34;minutemetrics.md&#34;&gt;MinuteMetrics&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### PrimaryAccessKey

Returns the &lt;code&gt;PrimaryAccessKey&lt;/code&gt; value.

#### PrimaryBlobConnectionString

Returns the &lt;code&gt;PrimaryBlobConnectionString&lt;/code&gt; value.

#### PrimaryBlobEndpoint

Returns the &lt;code&gt;PrimaryBlobEndpoint&lt;/code&gt; value.

#### PrimaryBlobHost

Returns the &lt;code&gt;PrimaryBlobHost&lt;/code&gt; value.

#### PrimaryConnectionString

Returns the &lt;code&gt;PrimaryConnectionString&lt;/code&gt; value.

#### PrimaryDfsEndpoint

Returns the &lt;code&gt;PrimaryDfsEndpoint&lt;/code&gt; value.

#### PrimaryDfsHost

Returns the &lt;code&gt;PrimaryDfsHost&lt;/code&gt; value.

#### PrimaryFileEndpoint

Returns the &lt;code&gt;PrimaryFileEndpoint&lt;/code&gt; value.

#### PrimaryFileHost

Returns the &lt;code&gt;PrimaryFileHost&lt;/code&gt; value.

#### PrimaryLocation

Returns the &lt;code&gt;PrimaryLocation&lt;/code&gt; value.

#### PrimaryQueueEndpoint

Returns the &lt;code&gt;PrimaryQueueEndpoint&lt;/code&gt; value.

#### PrimaryQueueHost

Returns the &lt;code&gt;PrimaryQueueHost&lt;/code&gt; value.

#### PrimaryTableEndpoint

Returns the &lt;code&gt;PrimaryTableEndpoint&lt;/code&gt; value.

#### PrimaryTableHost

Returns the &lt;code&gt;PrimaryTableHost&lt;/code&gt; value.

#### PrimaryWebEndpoint

Returns the &lt;code&gt;PrimaryWebEndpoint&lt;/code&gt; value.

#### PrimaryWebHost

Returns the &lt;code&gt;PrimaryWebHost&lt;/code&gt; value.

#### SecondaryAccessKey

Returns the &lt;code&gt;SecondaryAccessKey&lt;/code&gt; value.

#### SecondaryBlobConnectionString

Returns the &lt;code&gt;SecondaryBlobConnectionString&lt;/code&gt; value.

#### SecondaryBlobEndpoint

Returns the &lt;code&gt;SecondaryBlobEndpoint&lt;/code&gt; value.

#### SecondaryBlobHost

Returns the &lt;code&gt;SecondaryBlobHost&lt;/code&gt; value.

#### SecondaryConnectionString

Returns the &lt;code&gt;SecondaryConnectionString&lt;/code&gt; value.

#### SecondaryDfsEndpoint

Returns the &lt;code&gt;SecondaryDfsEndpoint&lt;/code&gt; value.

#### SecondaryDfsHost

Returns the &lt;code&gt;SecondaryDfsHost&lt;/code&gt; value.

#### SecondaryFileEndpoint

Returns the &lt;code&gt;SecondaryFileEndpoint&lt;/code&gt; value.

#### SecondaryFileHost

Returns the &lt;code&gt;SecondaryFileHost&lt;/code&gt; value.

#### SecondaryLocation

Returns the &lt;code&gt;SecondaryLocation&lt;/code&gt; value.

#### SecondaryQueueEndpoint

Returns the &lt;code&gt;SecondaryQueueEndpoint&lt;/code&gt; value.

#### SecondaryQueueHost

Returns the &lt;code&gt;SecondaryQueueHost&lt;/code&gt; value.

#### SecondaryTableEndpoint

Returns the &lt;code&gt;SecondaryTableEndpoint&lt;/code&gt; value.

#### SecondaryTableHost

Returns the &lt;code&gt;SecondaryTableHost&lt;/code&gt; value.

#### SecondaryWebEndpoint

Returns the &lt;code&gt;SecondaryWebEndpoint&lt;/code&gt; value.

#### SecondaryWebHost

Returns the &lt;code&gt;SecondaryWebHost&lt;/code&gt; value.

