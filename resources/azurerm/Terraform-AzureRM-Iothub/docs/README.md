# Terraform::AzureRM::Iothub

CloudFormation equivalent of azurerm_iothub

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::Iothub",
    "Properties" : {
        "<a href="#eventhubpartitioncount" title="EventHubPartitionCount">EventHubPartitionCount</a>" : <i>Double</i>,
        "<a href="#eventhubretentionindays" title="EventHubRetentionInDays">EventHubRetentionInDays</a>" : <i>Double</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>[ &lt;a href=&#34;endpoint.md&#34;&gt;Endpoint&lt;/a&gt;, ... ]</i>,
        "<a href="#fallbackroute" title="FallbackRoute">FallbackRoute</a>" : <i>[ &lt;a href=&#34;fallbackroute.md&#34;&gt;FallbackRoute&lt;/a&gt;, ... ]</i>,
        "<a href="#fileupload" title="FileUpload">FileUpload</a>" : <i>[ &lt;a href=&#34;fileupload.md&#34;&gt;FileUpload&lt;/a&gt;, ... ]</i>,
        "<a href="#ipfilterrule" title="IpFilterRule">IpFilterRule</a>" : <i>[ &lt;a href=&#34;ipfilterrule.md&#34;&gt;IpFilterRule&lt;/a&gt;, ... ]</i>,
        "<a href="#route" title="Route">Route</a>" : <i>[ &lt;a href=&#34;route.md&#34;&gt;Route&lt;/a&gt;, ... ]</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>[ &lt;a href=&#34;sku.md&#34;&gt;Sku&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::Iothub
Properties:
    <a href="#eventhubpartitioncount" title="EventHubPartitionCount">EventHubPartitionCount</a>: <i>Double</i>
    <a href="#eventhubretentionindays" title="EventHubRetentionInDays">EventHubRetentionInDays</a>: <i>Double</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>
      - &lt;a href=&#34;endpoint.md&#34;&gt;Endpoint&lt;/a&gt;</i>
    <a href="#fallbackroute" title="FallbackRoute">FallbackRoute</a>: <i>
      - &lt;a href=&#34;fallbackroute.md&#34;&gt;FallbackRoute&lt;/a&gt;</i>
    <a href="#fileupload" title="FileUpload">FileUpload</a>: <i>
      - &lt;a href=&#34;fileupload.md&#34;&gt;FileUpload&lt;/a&gt;</i>
    <a href="#ipfilterrule" title="IpFilterRule">IpFilterRule</a>: <i>
      - &lt;a href=&#34;ipfilterrule.md&#34;&gt;IpFilterRule&lt;/a&gt;</i>
    <a href="#route" title="Route">Route</a>: <i>
      - &lt;a href=&#34;route.md&#34;&gt;Route&lt;/a&gt;</i>
    <a href="#sku" title="Sku">Sku</a>: <i>
      - &lt;a href=&#34;sku.md&#34;&gt;Sku&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### EventHubPartitionCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventHubRetentionInDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

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

#### Endpoint

_Required_: No

_Type_: List of &lt;a href=&#34;endpoint.md&#34;&gt;Endpoint&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackRoute

_Required_: No

_Type_: List of &lt;a href=&#34;fallbackroute.md&#34;&gt;FallbackRoute&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileUpload

_Required_: No

_Type_: List of &lt;a href=&#34;fileupload.md&#34;&gt;FileUpload&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpFilterRule

_Required_: No

_Type_: List of &lt;a href=&#34;ipfilterrule.md&#34;&gt;IpFilterRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Route

_Required_: No

_Type_: List of &lt;a href=&#34;route.md&#34;&gt;Route&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

_Required_: No

_Type_: List of &lt;a href=&#34;sku.md&#34;&gt;Sku&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

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

Returns the &lt;code&gt;EventHubEventsEndpoint&lt;/code&gt; value.

#### EventHubEventsPath

Returns the &lt;code&gt;EventHubEventsPath&lt;/code&gt; value.

#### EventHubOperationsEndpoint

Returns the &lt;code&gt;EventHubOperationsEndpoint&lt;/code&gt; value.

#### EventHubOperationsPath

Returns the &lt;code&gt;EventHubOperationsPath&lt;/code&gt; value.

#### Hostname

Returns the &lt;code&gt;Hostname&lt;/code&gt; value.

#### SharedAccessPolicy

Returns the &lt;code&gt;SharedAccessPolicy&lt;/code&gt; value.

#### Type

Returns the &lt;code&gt;Type&lt;/code&gt; value.

