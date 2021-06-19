# TF::Thunder::SlbTemplateHttp RedirectRewriteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#redirectsecure" title="RedirectSecure">RedirectSecure</a>" : <i>Double</i>,
    "<a href="#redirectsecureport" title="RedirectSecurePort">RedirectSecurePort</a>" : <i>Double</i>,
    "<a href="#matchlist" title="MatchList">MatchList</a>" : <i>[ <a href="matchlistdefinition.md">MatchListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#redirectsecure" title="RedirectSecure">RedirectSecure</a>: <i>Double</i>
<a href="#redirectsecureport" title="RedirectSecurePort">RedirectSecurePort</a>: <i>Double</i>
<a href="#matchlist" title="MatchList">MatchList</a>: <i>
      - <a href="matchlistdefinition.md">MatchListDefinition</a></i>
</pre>

## Properties

#### RedirectSecure

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectSecurePort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchList

_Required_: No

_Type_: List of <a href="matchlistdefinition.md">MatchListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

