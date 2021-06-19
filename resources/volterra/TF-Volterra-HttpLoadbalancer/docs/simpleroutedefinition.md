# TF::Volterra::HttpLoadbalancer SimpleRouteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autohostrewrite" title="AutoHostRewrite">AutoHostRewrite</a>" : <i>Boolean</i>,
    "<a href="#disablehostrewrite" title="DisableHostRewrite">DisableHostRewrite</a>" : <i>Boolean</i>,
    "<a href="#hostrewrite" title="HostRewrite">HostRewrite</a>" : <i>String</i>,
    "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>[ <a href="httpmethoddefinition.md">HttpMethodDefinition</a>, ... ]</i>,
    "<a href="#advancedoptions" title="AdvancedOptions">AdvancedOptions</a>" : <i>[ <a href="advancedoptionsdefinition.md">AdvancedOptionsDefinition</a>, ... ]</i>,
    "<a href="#originpools" title="OriginPools">OriginPools</a>" : <i>[ <a href="originpoolsdefinition.md">OriginPoolsDefinition</a>, ... ]</i>,
    "<a href="#path" title="Path">Path</a>" : <i>[ <a href="pathdefinition.md">PathDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autohostrewrite" title="AutoHostRewrite">AutoHostRewrite</a>: <i>Boolean</i>
<a href="#disablehostrewrite" title="DisableHostRewrite">DisableHostRewrite</a>: <i>Boolean</i>
<a href="#hostrewrite" title="HostRewrite">HostRewrite</a>: <i>String</i>
<a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>
      - <a href="httpmethoddefinition.md">HttpMethodDefinition</a></i>
<a href="#advancedoptions" title="AdvancedOptions">AdvancedOptions</a>: <i>
      - <a href="advancedoptionsdefinition.md">AdvancedOptionsDefinition</a></i>
<a href="#originpools" title="OriginPools">OriginPools</a>: <i>
      - <a href="originpoolsdefinition.md">OriginPoolsDefinition</a></i>
<a href="#path" title="Path">Path</a>: <i>
      - <a href="pathdefinition.md">PathDefinition</a></i>
</pre>

## Properties

#### AutoHostRewrite

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableHostRewrite

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostRewrite

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMethod

_Required_: No

_Type_: List of <a href="httpmethoddefinition.md">HttpMethodDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvancedOptions

_Required_: No

_Type_: List of <a href="advancedoptionsdefinition.md">AdvancedOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginPools

_Required_: No

_Type_: List of <a href="originpoolsdefinition.md">OriginPoolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: List of <a href="pathdefinition.md">PathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

