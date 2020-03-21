# Terraform::AWS::AlbListener DefaultAction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
    "<a href="#targetgrouparn" title="TargetGroupArn">TargetGroupArn</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>" : <i>[ &lt;a href=&#34;defaultaction-authenticatecognito.md&#34;&gt;AuthenticateCognito&lt;/a&gt;, ... ]</i>,
    "<a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>" : <i>[ &lt;a href=&#34;defaultaction-authenticateoidc.md&#34;&gt;AuthenticateOidc&lt;/a&gt;, ... ]</i>,
    "<a href="#fixedresponse" title="FixedResponse">FixedResponse</a>" : <i>[ &lt;a href=&#34;defaultaction-fixedresponse.md&#34;&gt;FixedResponse&lt;/a&gt;, ... ]</i>,
    "<a href="#redirect" title="Redirect">Redirect</a>" : <i>[ &lt;a href=&#34;defaultaction-redirect.md&#34;&gt;Redirect&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#order" title="Order">Order</a>: <i>Double</i>
<a href="#targetgrouparn" title="TargetGroupArn">TargetGroupArn</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>: <i>
      - &lt;a href=&#34;defaultaction-authenticatecognito.md&#34;&gt;AuthenticateCognito&lt;/a&gt;</i>
<a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>: <i>
      - &lt;a href=&#34;defaultaction-authenticateoidc.md&#34;&gt;AuthenticateOidc&lt;/a&gt;</i>
<a href="#fixedresponse" title="FixedResponse">FixedResponse</a>: <i>
      - &lt;a href=&#34;defaultaction-fixedresponse.md&#34;&gt;FixedResponse&lt;/a&gt;</i>
<a href="#redirect" title="Redirect">Redirect</a>: <i>
      - &lt;a href=&#34;defaultaction-redirect.md&#34;&gt;Redirect&lt;/a&gt;</i>
</pre>

## Properties

#### Order

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupArn

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateCognito

_Required_: No
_Type_: List of &lt;a href=&#34;defaultaction-authenticatecognito.md&#34;&gt;AuthenticateCognito&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateOidc

_Required_: No
_Type_: List of &lt;a href=&#34;defaultaction-authenticateoidc.md&#34;&gt;AuthenticateOidc&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedResponse

_Required_: No
_Type_: List of &lt;a href=&#34;defaultaction-fixedresponse.md&#34;&gt;FixedResponse&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redirect

_Required_: No
_Type_: List of &lt;a href=&#34;defaultaction-redirect.md&#34;&gt;Redirect&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

