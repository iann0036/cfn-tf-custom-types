# Terraform::OCI::ApigatewayDeployment

CloudFormation equivalent of oci_apigateway_deployment

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::ApigatewayDeployment",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;, ... ]</i>,
        "<a href="#gatewayid" title="GatewayId">GatewayId</a>" : <i>String</i>,
        "<a href="#lifecycledetails" title="LifecycleDetails">LifecycleDetails</a>" : <i>String</i>,
        "<a href="#pathprefix" title="PathPrefix">PathPrefix</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#timecreated" title="TimeCreated">TimeCreated</a>" : <i>String</i>,
        "<a href="#timeupdated" title="TimeUpdated">TimeUpdated</a>" : <i>String</i>,
        "<a href="#specification" title="Specification">Specification</a>" : <i>[ &lt;a href=&#34;specification.md&#34;&gt;Specification&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#loggingpolicies" title="LoggingPolicies">LoggingPolicies</a>" : <i>[ &lt;a href=&#34;loggingpolicies.md&#34;&gt;LoggingPolicies&lt;/a&gt;, ... ]</i>,
        "<a href="#requestpolicies" title="RequestPolicies">RequestPolicies</a>" : <i>[ &lt;a href=&#34;requestpolicies.md&#34;&gt;RequestPolicies&lt;/a&gt;, ... ]</i>,
        "<a href="#routes" title="Routes">Routes</a>" : <i>[ &lt;a href=&#34;routes.md&#34;&gt;Routes&lt;/a&gt;, ... ]</i>,
        "<a href="#accesslog" title="AccessLog">AccessLog</a>" : <i>[ &lt;a href=&#34;accesslog.md&#34;&gt;AccessLog&lt;/a&gt;, ... ]</i>,
        "<a href="#executionlog" title="ExecutionLog">ExecutionLog</a>" : <i>[ &lt;a href=&#34;executionlog.md&#34;&gt;ExecutionLog&lt;/a&gt;, ... ]</i>,
        "<a href="#authentication" title="Authentication">Authentication</a>" : <i>[ &lt;a href=&#34;authentication.md&#34;&gt;Authentication&lt;/a&gt;, ... ]</i>,
        "<a href="#cors" title="Cors">Cors</a>" : <i>[ &lt;a href=&#34;cors.md&#34;&gt;Cors&lt;/a&gt;, ... ]</i>,
        "<a href="#ratelimiting" title="RateLimiting">RateLimiting</a>" : <i>[ &lt;a href=&#34;ratelimiting.md&#34;&gt;RateLimiting&lt;/a&gt;, ... ]</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>[ &lt;a href=&#34;backend.md&#34;&gt;Backend&lt;/a&gt;, ... ]</i>,
        "<a href="#headers" title="Headers">Headers</a>" : <i>[ &lt;a href=&#34;headers.md&#34;&gt;Headers&lt;/a&gt;, ... ]</i>,
        "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ &lt;a href=&#34;authorization.md&#34;&gt;Authorization&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::ApigatewayDeployment
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;</i>
    <a href="#gatewayid" title="GatewayId">GatewayId</a>: <i>String</i>
    <a href="#lifecycledetails" title="LifecycleDetails">LifecycleDetails</a>: <i>String</i>
    <a href="#pathprefix" title="PathPrefix">PathPrefix</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#timecreated" title="TimeCreated">TimeCreated</a>: <i>String</i>
    <a href="#timeupdated" title="TimeUpdated">TimeUpdated</a>: <i>String</i>
    <a href="#specification" title="Specification">Specification</a>: <i>
      - &lt;a href=&#34;specification.md&#34;&gt;Specification&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#loggingpolicies" title="LoggingPolicies">LoggingPolicies</a>: <i>
      - &lt;a href=&#34;loggingpolicies.md&#34;&gt;LoggingPolicies&lt;/a&gt;</i>
    <a href="#requestpolicies" title="RequestPolicies">RequestPolicies</a>: <i>
      - &lt;a href=&#34;requestpolicies.md&#34;&gt;RequestPolicies&lt;/a&gt;</i>
    <a href="#routes" title="Routes">Routes</a>: <i>
      - &lt;a href=&#34;routes.md&#34;&gt;Routes&lt;/a&gt;</i>
    <a href="#accesslog" title="AccessLog">AccessLog</a>: <i>
      - &lt;a href=&#34;accesslog.md&#34;&gt;AccessLog&lt;/a&gt;</i>
    <a href="#executionlog" title="ExecutionLog">ExecutionLog</a>: <i>
      - &lt;a href=&#34;executionlog.md&#34;&gt;ExecutionLog&lt;/a&gt;</i>
    <a href="#authentication" title="Authentication">Authentication</a>: <i>
      - &lt;a href=&#34;authentication.md&#34;&gt;Authentication&lt;/a&gt;</i>
    <a href="#cors" title="Cors">Cors</a>: <i>
      - &lt;a href=&#34;cors.md&#34;&gt;Cors&lt;/a&gt;</i>
    <a href="#ratelimiting" title="RateLimiting">RateLimiting</a>: <i>
      - &lt;a href=&#34;ratelimiting.md&#34;&gt;RateLimiting&lt;/a&gt;</i>
    <a href="#backend" title="Backend">Backend</a>: <i>
      - &lt;a href=&#34;backend.md&#34;&gt;Backend&lt;/a&gt;</i>
    <a href="#headers" title="Headers">Headers</a>: <i>
      - &lt;a href=&#34;headers.md&#34;&gt;Headers&lt;/a&gt;</i>
    <a href="#authorization" title="Authorization">Authorization</a>: <i>
      - &lt;a href=&#34;authorization.md&#34;&gt;Authorization&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleDetails

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathPrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeCreated

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeUpdated

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Specification

_Required_: No

_Type_: List of &lt;a href=&#34;specification.md&#34;&gt;Specification&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingPolicies

_Required_: No

_Type_: List of &lt;a href=&#34;loggingpolicies.md&#34;&gt;LoggingPolicies&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestPolicies

_Required_: No

_Type_: List of &lt;a href=&#34;requestpolicies.md&#34;&gt;RequestPolicies&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routes

_Required_: No

_Type_: List of &lt;a href=&#34;routes.md&#34;&gt;Routes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessLog

_Required_: No

_Type_: List of &lt;a href=&#34;accesslog.md&#34;&gt;AccessLog&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionLog

_Required_: No

_Type_: List of &lt;a href=&#34;executionlog.md&#34;&gt;ExecutionLog&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentication

_Required_: No

_Type_: List of &lt;a href=&#34;authentication.md&#34;&gt;Authentication&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: List of &lt;a href=&#34;cors.md&#34;&gt;Cors&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimiting

_Required_: No

_Type_: List of &lt;a href=&#34;ratelimiting.md&#34;&gt;RateLimiting&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No

_Type_: List of &lt;a href=&#34;backend.md&#34;&gt;Backend&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of &lt;a href=&#34;headers.md&#34;&gt;Headers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authorization

_Required_: No

_Type_: List of &lt;a href=&#34;authorization.md&#34;&gt;Authorization&lt;/a&gt;

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

#### LifecycleDetails

Returns the &lt;code&gt;LifecycleDetails&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### TimeCreated

Returns the &lt;code&gt;TimeCreated&lt;/code&gt; value.

#### TimeUpdated

Returns the &lt;code&gt;TimeUpdated&lt;/code&gt; value.

