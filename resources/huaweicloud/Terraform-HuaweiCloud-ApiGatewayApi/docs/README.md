# Terraform::HuaweiCloud::ApiGatewayApi

Provides an API gateway API resource.

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
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#requestmethod" title="RequestMethod">RequestMethod</a>" : <i>String</i>,
        "<a href="#requestprotocol" title="RequestProtocol">RequestProtocol</a>" : <i>String</i>,
        "<a href="#requesturi" title="RequestUri">RequestUri</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>Double</i>,
        "<a href="#backendparameter" title="BackendParameter">BackendParameter</a>" : <i>[ <a href="backendparameter.md">BackendParameter</a>, ... ]</i>,
        "<a href="#functionbackend" title="FunctionBackend">FunctionBackend</a>" : <i>[ <a href="functionbackend.md">FunctionBackend</a>, ... ]</i>,
        "<a href="#httpbackend" title="HttpBackend">HttpBackend</a>" : <i>[ <a href="httpbackend.md">HttpBackend</a>, ... ]</i>,
        "<a href="#mockbackend" title="MockBackend">MockBackend</a>" : <i>[ <a href="mockbackend.md">MockBackend</a>, ... ]</i>,
        "<a href="#requestparameter" title="RequestParameter">RequestParameter</a>" : <i>[ <a href="requestparameter.md">RequestParameter</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
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
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#requestmethod" title="RequestMethod">RequestMethod</a>: <i>String</i>
    <a href="#requestprotocol" title="RequestProtocol">RequestProtocol</a>: <i>String</i>
    <a href="#requesturi" title="RequestUri">RequestUri</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>Double</i>
    <a href="#backendparameter" title="BackendParameter">BackendParameter</a>: <i>
      - <a href="backendparameter.md">BackendParameter</a></i>
    <a href="#functionbackend" title="FunctionBackend">FunctionBackend</a>: <i>
      - <a href="functionbackend.md">FunctionBackend</a></i>
    <a href="#httpbackend" title="HttpBackend">HttpBackend</a>: <i>
      - <a href="httpbackend.md">HttpBackend</a></i>
    <a href="#mockbackend" title="MockBackend">MockBackend</a>: <i>
      - <a href="mockbackend.md">MockBackend</a></i>
    <a href="#requestparameter" title="RequestParameter">RequestParameter</a>: <i>
      - <a href="requestparameter.md">RequestParameter</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AuthType

Specifies the security authentication mode.
The value can be 'App', 'IAM', and 'NONE'.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendType

Specifies the service backend type. The value can be:
- 'HTTP': the web service backend
- 'FUNCTION': the FunctionGraph service backend
- 'MOCK': the Mock service backend.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

Specifies whether CORS is supported or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Specifies the description of the API.
The description cannot exceed 255 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExampleFailureResponse

Specifies the example response for a failed request
The length cannot exceed 20,480 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExampleSuccessResponse

Specifies the example response for a successful request.
The length cannot exceed 20,480 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

Specifies the ID of the API group.
Changing this creates a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the API. An API name consists of 3–64 characters,
starting with a letter. Only letters, digits, and underscores (_) are allowed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestMethod

Specifies the request method, including 'GET','POST','PUT' and etc..

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestProtocol

Specifies the request protocol. The value can be 'HTTP', 'HTTPS', and 'BOTH'
which means the API can be accessed through both 'HTTP' and 'HTTPS'. Defaults to 'HTTPS'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestUri

Specifies the request path of the API. The value must comply with URI specifications.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

the tags of API in format of string list.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Specifies the version of the API. A maximum of 16 characters are allowed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

Specifies whether the API is available to the public.
The value can be 1 (public) and 2 (private). Defaults to 2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendParameter

_Required_: No

_Type_: List of <a href="backendparameter.md">BackendParameter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionBackend

_Required_: No

_Type_: List of <a href="functionbackend.md">FunctionBackend</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpBackend

_Required_: No

_Type_: List of <a href="httpbackend.md">HttpBackend</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MockBackend

_Required_: No

_Type_: List of <a href="mockbackend.md">MockBackend</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestParameter

_Required_: No

_Type_: List of <a href="requestparameter.md">RequestParameter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

Returns the <code>GroupName</code> value.

#### Id

Returns the <code>Id</code> value.

