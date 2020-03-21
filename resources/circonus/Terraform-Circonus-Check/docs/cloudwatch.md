# Terraform::Circonus::Check Cloudwatch

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#apikey" title="ApiKey">ApiKey</a>" : <i>String</i>,
    "<a href="#apisecret" title="ApiSecret">ApiSecret</a>" : <i>String</i>,
    "<a href="#dimmensions" title="Dimmensions">Dimmensions</a>" : <i>[ &lt;a href=&#34;cloudwatch-dimmensions.md&#34;&gt;Dimmensions&lt;/a&gt;, ... ]</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>[ String, ... ]</i>,
    "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#apikey" title="ApiKey">ApiKey</a>: <i>String</i>
<a href="#apisecret" title="ApiSecret">ApiSecret</a>: <i>String</i>
<a href="#dimmensions" title="Dimmensions">Dimmensions</a>: <i>
      - &lt;a href=&#34;cloudwatch-dimmensions.md&#34;&gt;Dimmensions&lt;/a&gt;</i>
<a href="#metric" title="Metric">Metric</a>: <i>
      - String</i>
<a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### ApiKey

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiSecret

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimmensions

_Required_: Yes
_Type_: List of &lt;a href=&#34;cloudwatch-dimmensions.md&#34;&gt;Dimmensions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

