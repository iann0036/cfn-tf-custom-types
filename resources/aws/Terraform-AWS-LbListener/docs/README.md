# Terraform::AWS::LbListener

CloudFormation equivalent of aws_lb_listener

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LbListener",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#certificatearn" title="CertificateArn">CertificateArn</a>" : <i>String</i>,
        "<a href="#loadbalancerarn" title="LoadBalancerArn">LoadBalancerArn</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#sslpolicy" title="SslPolicy">SslPolicy</a>" : <i>String</i>,
        "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>[ &lt;a href=&#34;defaultaction.md&#34;&gt;DefaultAction&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>" : <i>[ &lt;a href=&#34;authenticatecognito.md&#34;&gt;AuthenticateCognito&lt;/a&gt;, ... ]</i>,
        "<a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>" : <i>[ &lt;a href=&#34;authenticateoidc.md&#34;&gt;AuthenticateOidc&lt;/a&gt;, ... ]</i>,
        "<a href="#fixedresponse" title="FixedResponse">FixedResponse</a>" : <i>[ &lt;a href=&#34;fixedresponse.md&#34;&gt;FixedResponse&lt;/a&gt;, ... ]</i>,
        "<a href="#redirect" title="Redirect">Redirect</a>" : <i>[ &lt;a href=&#34;redirect.md&#34;&gt;Redirect&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LbListener
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#certificatearn" title="CertificateArn">CertificateArn</a>: <i>String</i>
    <a href="#loadbalancerarn" title="LoadBalancerArn">LoadBalancerArn</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#sslpolicy" title="SslPolicy">SslPolicy</a>: <i>String</i>
    <a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>
      - &lt;a href=&#34;defaultaction.md&#34;&gt;DefaultAction&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>: <i>
      - &lt;a href=&#34;authenticatecognito.md&#34;&gt;AuthenticateCognito&lt;/a&gt;</i>
    <a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>: <i>
      - &lt;a href=&#34;authenticateoidc.md&#34;&gt;AuthenticateOidc&lt;/a&gt;</i>
    <a href="#fixedresponse" title="FixedResponse">FixedResponse</a>: <i>
      - &lt;a href=&#34;fixedresponse.md&#34;&gt;FixedResponse&lt;/a&gt;</i>
    <a href="#redirect" title="Redirect">Redirect</a>: <i>
      - &lt;a href=&#34;redirect.md&#34;&gt;Redirect&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAction

_Required_: No

_Type_: List of &lt;a href=&#34;defaultaction.md&#34;&gt;DefaultAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateCognito

_Required_: No

_Type_: List of &lt;a href=&#34;authenticatecognito.md&#34;&gt;AuthenticateCognito&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateOidc

_Required_: No

_Type_: List of &lt;a href=&#34;authenticateoidc.md&#34;&gt;AuthenticateOidc&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedResponse

_Required_: No

_Type_: List of &lt;a href=&#34;fixedresponse.md&#34;&gt;FixedResponse&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redirect

_Required_: No

_Type_: List of &lt;a href=&#34;redirect.md&#34;&gt;Redirect&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

