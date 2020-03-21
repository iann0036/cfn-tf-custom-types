# Terraform::AzureRM::AppConfiguration

CloudFormation equivalent of azurerm_app_configuration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::AppConfiguration",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#primaryreadkey" title="PrimaryReadKey">PrimaryReadKey</a>" : <i>[ &lt;a href=&#34;primaryreadkey.md&#34;&gt;PrimaryReadKey&lt;/a&gt;, ... ]</i>,
        "<a href="#primarywritekey" title="PrimaryWriteKey">PrimaryWriteKey</a>" : <i>[ &lt;a href=&#34;primarywritekey.md&#34;&gt;PrimaryWriteKey&lt;/a&gt;, ... ]</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#secondaryreadkey" title="SecondaryReadKey">SecondaryReadKey</a>" : <i>[ &lt;a href=&#34;secondaryreadkey.md&#34;&gt;SecondaryReadKey&lt;/a&gt;, ... ]</i>,
        "<a href="#secondarywritekey" title="SecondaryWriteKey">SecondaryWriteKey</a>" : <i>[ &lt;a href=&#34;secondarywritekey.md&#34;&gt;SecondaryWriteKey&lt;/a&gt;, ... ]</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::AppConfiguration
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#primaryreadkey" title="PrimaryReadKey">PrimaryReadKey</a>: <i>
      - &lt;a href=&#34;primaryreadkey.md&#34;&gt;PrimaryReadKey&lt;/a&gt;</i>
    <a href="#primarywritekey" title="PrimaryWriteKey">PrimaryWriteKey</a>: <i>
      - &lt;a href=&#34;primarywritekey.md&#34;&gt;PrimaryWriteKey&lt;/a&gt;</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#secondaryreadkey" title="SecondaryReadKey">SecondaryReadKey</a>: <i>
      - &lt;a href=&#34;secondaryreadkey.md&#34;&gt;SecondaryReadKey&lt;/a&gt;</i>
    <a href="#secondarywritekey" title="SecondaryWriteKey">SecondaryWriteKey</a>: <i>
      - &lt;a href=&#34;secondarywritekey.md&#34;&gt;SecondaryWriteKey&lt;/a&gt;</i>
    <a href="#sku" title="Sku">Sku</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

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

#### PrimaryReadKey

_Required_: No

_Type_: List of &lt;a href=&#34;primaryreadkey.md&#34;&gt;PrimaryReadKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryWriteKey

_Required_: No

_Type_: List of &lt;a href=&#34;primarywritekey.md&#34;&gt;PrimaryWriteKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryReadKey

_Required_: No

_Type_: List of &lt;a href=&#34;secondaryreadkey.md&#34;&gt;SecondaryReadKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryWriteKey

_Required_: No

_Type_: List of &lt;a href=&#34;secondarywritekey.md&#34;&gt;SecondaryWriteKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

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

#### Endpoint

Returns the &lt;code&gt;Endpoint&lt;/code&gt; value.

#### PrimaryReadKey

Returns the &lt;code&gt;PrimaryReadKey&lt;/code&gt; value.

#### PrimaryWriteKey

Returns the &lt;code&gt;PrimaryWriteKey&lt;/code&gt; value.

#### SecondaryReadKey

Returns the &lt;code&gt;SecondaryReadKey&lt;/code&gt; value.

#### SecondaryWriteKey

Returns the &lt;code&gt;SecondaryWriteKey&lt;/code&gt; value.

