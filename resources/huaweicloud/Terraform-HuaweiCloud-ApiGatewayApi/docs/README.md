# Terraform::HuaweiCloud::ApiGatewayApi

CloudFormation equivalent of huaweicloud_api_gateway_api

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::ApiGatewayApi",
    "Properties" : {
        "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
        "<a href="#backendtype" title="BackendType">BackendType</a>" : <i>String</i>,
        "<a href="#cors" title="Cors">Cors</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#examplefailureresponse" title="ExampleFailureResponse">ExampleFailureResponse</a>" : <i>String</i>,
        "<a href="#examplesuccessresponse" title="ExampleSuccessResponse">ExampleSuccessResponse</a>" : <i>String</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#requestmethod" title="RequestMethod">RequestMethod</a>" : <i>String</i>,
        "<a href="#requestprotocol" title="RequestProtocol">RequestProtocol</a>" : <i>String</i>,
        "<a href="#requesturi" title="RequestUri">RequestUri</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>Double</i>,
        "<a href="#backendparameter" title="BackendParameter">BackendParameter</a>" : <i>[ &lt;a href=&#34;backendparameter.md&#34;&gt;BackendParameter&lt;/a&gt;, ... ]</i>,
        "<a href="#functionbackend" title="FunctionBackend">FunctionBackend</a>" : <i>[ &lt;a href=&#34;functionbackend.md&#34;&gt;FunctionBackend&lt;/a&gt;, ... ]</i>,
        "<a href="#httpbackend" title="HttpBackend">HttpBackend</a>" : <i>[ &lt;a href=&#34;httpbackend.md&#34;&gt;HttpBackend&lt;/a&gt;, ... ]</i>,
        "<a href="#mockbackend" title="MockBackend">MockBackend</a>" : <i>[ &lt;a href=&#34;mockbackend.md&#34;&gt;MockBackend&lt;/a&gt;, ... ]</i>,
        "<a href="#requestparameter" title="RequestParameter">RequestParameter</a>" : <i>[ &lt;a href=&#34;requestparameter.md&#34;&gt;RequestParameter&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::ApiGatewayApi
Properties:
    <a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
    <a href="#backendtype" title="BackendType">BackendType</a>: <i>String</i>
    <a href="#cors" title="Cors">Cors</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#examplefailureresponse" title="ExampleFailureResponse">ExampleFailureResponse</a>: <i>String</i>
    <a href="#examplesuccessresponse" title="ExampleSuccessResponse">ExampleSuccessResponse</a>: <i>String</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#requestmethod" title="RequestMethod">RequestMethod</a>: <i>String</i>
    <a href="#requestprotocol" title="RequestProtocol">RequestProtocol</a>: <i>String</i>
    <a href="#requesturi" title="RequestUri">RequestUri</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>Double</i>
    <a href="#backendparameter" title="BackendParameter">BackendParameter</a>: <i>
      - &lt;a href=&#34;backendparameter.md&#34;&gt;BackendParameter&lt;/a&gt;</i>
    <a href="#functionbackend" title="FunctionBackend">FunctionBackend</a>: <i>
      - &lt;a href=&#34;functionbackend.md&#34;&gt;FunctionBackend&lt;/a&gt;</i>
    <a href="#httpbackend" title="HttpBackend">HttpBackend</a>: <i>
      - &lt;a href=&#34;httpbackend.md&#34;&gt;HttpBackend&lt;/a&gt;</i>
    <a href="#mockbackend" title="MockBackend">MockBackend</a>: <i>
      - &lt;a href=&#34;mockbackend.md&#34;&gt;MockBackend&lt;/a&gt;</i>
    <a href="#requestparameter" title="RequestParameter">RequestParameter</a>: <i>
      - &lt;a href=&#34;requestparameter.md&#34;&gt;RequestParameter&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### AuthType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExampleFailureResponse

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExampleSuccessResponse

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestMethod

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestUri

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendParameter

_Required_: No

_Type_: List of &lt;a href=&#34;backendparameter.md&#34;&gt;BackendParameter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionBackend

_Required_: No

_Type_: List of &lt;a href=&#34;functionbackend.md&#34;&gt;FunctionBackend&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpBackend

_Required_: No

_Type_: List of &lt;a href=&#34;httpbackend.md&#34;&gt;HttpBackend&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MockBackend

_Required_: No

_Type_: List of &lt;a href=&#34;mockbackend.md&#34;&gt;MockBackend&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestParameter

_Required_: No

_Type_: List of &lt;a href=&#34;requestparameter.md&#34;&gt;RequestParameter&lt;/a&gt;

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

#### GroupName

Returns the &lt;code&gt;GroupName&lt;/code&gt; value.

