# Terraform::OCI::WaasWaasPolicy AccessRules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#blockaction" title="BlockAction">BlockAction</a>" : <i>String</i>,
    "<a href="#blockerrorpagecode" title="BlockErrorPageCode">BlockErrorPageCode</a>" : <i>String</i>,
    "<a href="#blockerrorpagedescription" title="BlockErrorPageDescription">BlockErrorPageDescription</a>" : <i>String</i>,
    "<a href="#blockerrorpagemessage" title="BlockErrorPageMessage">BlockErrorPageMessage</a>" : <i>String</i>,
    "<a href="#blockresponsecode" title="BlockResponseCode">BlockResponseCode</a>" : <i>Double</i>,
    "<a href="#bypasschallenges" title="BypassChallenges">BypassChallenges</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#redirectresponsecode" title="RedirectResponseCode">RedirectResponseCode</a>" : <i>String</i>,
    "<a href="#redirecturl" title="RedirectUrl">RedirectUrl</a>" : <i>String</i>,
    "<a href="#criteria" title="Criteria">Criteria</a>" : <i>[ &lt;a href=&#34;accessrules-criteria.md&#34;&gt;Criteria&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#blockaction" title="BlockAction">BlockAction</a>: <i>String</i>
<a href="#blockerrorpagecode" title="BlockErrorPageCode">BlockErrorPageCode</a>: <i>String</i>
<a href="#blockerrorpagedescription" title="BlockErrorPageDescription">BlockErrorPageDescription</a>: <i>String</i>
<a href="#blockerrorpagemessage" title="BlockErrorPageMessage">BlockErrorPageMessage</a>: <i>String</i>
<a href="#blockresponsecode" title="BlockResponseCode">BlockResponseCode</a>: <i>Double</i>
<a href="#bypasschallenges" title="BypassChallenges">BypassChallenges</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#redirectresponsecode" title="RedirectResponseCode">RedirectResponseCode</a>: <i>String</i>
<a href="#redirecturl" title="RedirectUrl">RedirectUrl</a>: <i>String</i>
<a href="#criteria" title="Criteria">Criteria</a>: <i>
      - &lt;a href=&#34;accessrules-criteria.md&#34;&gt;Criteria&lt;/a&gt;</i>
</pre>

## Properties

#### Action

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockAction

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockErrorPageCode

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockErrorPageDescription

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockErrorPageMessage

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockResponseCode

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BypassChallenges

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectResponseCode

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectUrl

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Criteria

_Required_: No
_Type_: List of &lt;a href=&#34;accessrules-criteria.md&#34;&gt;Criteria&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

