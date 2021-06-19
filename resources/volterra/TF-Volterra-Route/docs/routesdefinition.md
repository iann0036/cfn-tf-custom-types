# TF::Volterra::Route RoutesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disablecustomscript" title="DisableCustomScript">DisableCustomScript</a>" : <i>Boolean</i>,
    "<a href="#disablelocationadd" title="DisableLocationAdd">DisableLocationAdd</a>" : <i>Boolean</i>,
    "<a href="#requestheaderstoremove" title="RequestHeadersToRemove">RequestHeadersToRemove</a>" : <i>[ String, ... ]</i>,
    "<a href="#responseheaderstoremove" title="ResponseHeadersToRemove">ResponseHeadersToRemove</a>" : <i>[ String, ... ]</i>,
    "<a href="#match" title="Match">Match</a>" : <i>[ <a href="matchdefinition.md">MatchDefinition</a>, ... ]</i>,
    "<a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>" : <i>[ <a href="requestheaderstoadddefinition.md">RequestHeadersToAddDefinition</a>, ... ]</i>,
    "<a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>" : <i>[ <a href="responseheaderstoadddefinition.md">ResponseHeadersToAddDefinition</a>, ... ]</i>,
    "<a href="#routedestination" title="RouteDestination">RouteDestination</a>" : <i>[ <a href="routedestinationdefinition.md">RouteDestinationDefinition</a>, ... ]</i>,
    "<a href="#routedirectresponse" title="RouteDirectResponse">RouteDirectResponse</a>" : <i>[ <a href="routedirectresponsedefinition.md">RouteDirectResponseDefinition</a>, ... ]</i>,
    "<a href="#routeredirect" title="RouteRedirect">RouteRedirect</a>" : <i>[ <a href="routeredirectdefinition.md">RouteRedirectDefinition</a>, ... ]</i>,
    "<a href="#servicepolicy" title="ServicePolicy">ServicePolicy</a>" : <i>[ <a href="servicepolicydefinition.md">ServicePolicyDefinition</a>, ... ]</i>,
    "<a href="#waftype" title="WafType">WafType</a>" : <i>[ <a href="waftypedefinition.md">WafTypeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disablecustomscript" title="DisableCustomScript">DisableCustomScript</a>: <i>Boolean</i>
<a href="#disablelocationadd" title="DisableLocationAdd">DisableLocationAdd</a>: <i>Boolean</i>
<a href="#requestheaderstoremove" title="RequestHeadersToRemove">RequestHeadersToRemove</a>: <i>
      - String</i>
<a href="#responseheaderstoremove" title="ResponseHeadersToRemove">ResponseHeadersToRemove</a>: <i>
      - String</i>
<a href="#match" title="Match">Match</a>: <i>
      - <a href="matchdefinition.md">MatchDefinition</a></i>
<a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>: <i>
      - <a href="requestheaderstoadddefinition.md">RequestHeadersToAddDefinition</a></i>
<a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>: <i>
      - <a href="responseheaderstoadddefinition.md">ResponseHeadersToAddDefinition</a></i>
<a href="#routedestination" title="RouteDestination">RouteDestination</a>: <i>
      - <a href="routedestinationdefinition.md">RouteDestinationDefinition</a></i>
<a href="#routedirectresponse" title="RouteDirectResponse">RouteDirectResponse</a>: <i>
      - <a href="routedirectresponsedefinition.md">RouteDirectResponseDefinition</a></i>
<a href="#routeredirect" title="RouteRedirect">RouteRedirect</a>: <i>
      - <a href="routeredirectdefinition.md">RouteRedirectDefinition</a></i>
<a href="#servicepolicy" title="ServicePolicy">ServicePolicy</a>: <i>
      - <a href="servicepolicydefinition.md">ServicePolicyDefinition</a></i>
<a href="#waftype" title="WafType">WafType</a>: <i>
      - <a href="waftypedefinition.md">WafTypeDefinition</a></i>
</pre>

## Properties

#### DisableCustomScript

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableLocationAdd

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeadersToRemove

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeadersToRemove

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No

_Type_: List of <a href="matchdefinition.md">MatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeadersToAdd

_Required_: No

_Type_: List of <a href="requestheaderstoadddefinition.md">RequestHeadersToAddDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeadersToAdd

_Required_: No

_Type_: List of <a href="responseheaderstoadddefinition.md">ResponseHeadersToAddDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteDestination

_Required_: No

_Type_: List of <a href="routedestinationdefinition.md">RouteDestinationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteDirectResponse

_Required_: No

_Type_: List of <a href="routedirectresponsedefinition.md">RouteDirectResponseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteRedirect

_Required_: No

_Type_: List of <a href="routeredirectdefinition.md">RouteRedirectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePolicy

_Required_: No

_Type_: List of <a href="servicepolicydefinition.md">ServicePolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafType

_Required_: No

_Type_: List of <a href="waftypedefinition.md">WafTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

