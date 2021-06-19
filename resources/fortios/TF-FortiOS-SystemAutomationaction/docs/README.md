# TF::FortiOS::SystemAutomationaction

Action for automation stitches.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemAutomationaction",
    "Properties" : {
        "<a href="#accprofile" title="Accprofile">Accprofile</a>" : <i>String</i>,
        "<a href="#actiontype" title="ActionType">ActionType</a>" : <i>String</i>,
        "<a href="#alicloudaccesskeyid" title="AlicloudAccessKeyId">AlicloudAccessKeyId</a>" : <i>String</i>,
        "<a href="#alicloudaccesskeysecret" title="AlicloudAccessKeySecret">AlicloudAccessKeySecret</a>" : <i>String</i>,
        "<a href="#alicloudaccountid" title="AlicloudAccountId">AlicloudAccountId</a>" : <i>String</i>,
        "<a href="#alicloudfunction" title="AlicloudFunction">AlicloudFunction</a>" : <i>String</i>,
        "<a href="#alicloudfunctionauthorization" title="AlicloudFunctionAuthorization">AlicloudFunctionAuthorization</a>" : <i>String</i>,
        "<a href="#alicloudfunctiondomain" title="AlicloudFunctionDomain">AlicloudFunctionDomain</a>" : <i>String</i>,
        "<a href="#alicloudregion" title="AlicloudRegion">AlicloudRegion</a>" : <i>String</i>,
        "<a href="#alicloudservice" title="AlicloudService">AlicloudService</a>" : <i>String</i>,
        "<a href="#alicloudversion" title="AlicloudVersion">AlicloudVersion</a>" : <i>String</i>,
        "<a href="#awsapiid" title="AwsApiId">AwsApiId</a>" : <i>String</i>,
        "<a href="#awsapikey" title="AwsApiKey">AwsApiKey</a>" : <i>String</i>,
        "<a href="#awsapipath" title="AwsApiPath">AwsApiPath</a>" : <i>String</i>,
        "<a href="#awsapistage" title="AwsApiStage">AwsApiStage</a>" : <i>String</i>,
        "<a href="#awsdomain" title="AwsDomain">AwsDomain</a>" : <i>String</i>,
        "<a href="#awsregion" title="AwsRegion">AwsRegion</a>" : <i>String</i>,
        "<a href="#azureapikey" title="AzureApiKey">AzureApiKey</a>" : <i>String</i>,
        "<a href="#azureapp" title="AzureApp">AzureApp</a>" : <i>String</i>,
        "<a href="#azuredomain" title="AzureDomain">AzureDomain</a>" : <i>String</i>,
        "<a href="#azurefunction" title="AzureFunction">AzureFunction</a>" : <i>String</i>,
        "<a href="#azurefunctionauthorization" title="AzureFunctionAuthorization">AzureFunctionAuthorization</a>" : <i>String</i>,
        "<a href="#delay" title="Delay">Delay</a>" : <i>Double</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#emailbody" title="EmailBody">EmailBody</a>" : <i>String</i>,
        "<a href="#emailfrom" title="EmailFrom">EmailFrom</a>" : <i>String</i>,
        "<a href="#emailsubject" title="EmailSubject">EmailSubject</a>" : <i>String</i>,
        "<a href="#gcpfunction" title="GcpFunction">GcpFunction</a>" : <i>String</i>,
        "<a href="#gcpfunctiondomain" title="GcpFunctionDomain">GcpFunctionDomain</a>" : <i>String</i>,
        "<a href="#gcpfunctionregion" title="GcpFunctionRegion">GcpFunctionRegion</a>" : <i>String</i>,
        "<a href="#gcpproject" title="GcpProject">GcpProject</a>" : <i>String</i>,
        "<a href="#httpbody" title="HttpBody">HttpBody</a>" : <i>String</i>,
        "<a href="#message" title="Message">Message</a>" : <i>String</i>,
        "<a href="#method" title="Method">Method</a>" : <i>String</i>,
        "<a href="#minimuminterval" title="MinimumInterval">MinimumInterval</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#replacementmessage" title="ReplacementMessage">ReplacementMessage</a>" : <i>String</i>,
        "<a href="#required" title="Required">Required</a>" : <i>String</i>,
        "<a href="#script" title="Script">Script</a>" : <i>String</i>,
        "<a href="#securitytag" title="SecurityTag">SecurityTag</a>" : <i>String</i>,
        "<a href="#tlscertificate" title="TlsCertificate">TlsCertificate</a>" : <i>String</i>,
        "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#emailto" title="EmailTo">EmailTo</a>" : <i>[ <a href="emailtodefinition.md">EmailToDefinition</a>, ... ]</i>,
        "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>,
        "<a href="#sdnconnector" title="SdnConnector">SdnConnector</a>" : <i>[ <a href="sdnconnectordefinition.md">SdnConnectorDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemAutomationaction
Properties:
    <a href="#accprofile" title="Accprofile">Accprofile</a>: <i>String</i>
    <a href="#actiontype" title="ActionType">ActionType</a>: <i>String</i>
    <a href="#alicloudaccesskeyid" title="AlicloudAccessKeyId">AlicloudAccessKeyId</a>: <i>String</i>
    <a href="#alicloudaccesskeysecret" title="AlicloudAccessKeySecret">AlicloudAccessKeySecret</a>: <i>String</i>
    <a href="#alicloudaccountid" title="AlicloudAccountId">AlicloudAccountId</a>: <i>String</i>
    <a href="#alicloudfunction" title="AlicloudFunction">AlicloudFunction</a>: <i>String</i>
    <a href="#alicloudfunctionauthorization" title="AlicloudFunctionAuthorization">AlicloudFunctionAuthorization</a>: <i>String</i>
    <a href="#alicloudfunctiondomain" title="AlicloudFunctionDomain">AlicloudFunctionDomain</a>: <i>String</i>
    <a href="#alicloudregion" title="AlicloudRegion">AlicloudRegion</a>: <i>String</i>
    <a href="#alicloudservice" title="AlicloudService">AlicloudService</a>: <i>String</i>
    <a href="#alicloudversion" title="AlicloudVersion">AlicloudVersion</a>: <i>String</i>
    <a href="#awsapiid" title="AwsApiId">AwsApiId</a>: <i>String</i>
    <a href="#awsapikey" title="AwsApiKey">AwsApiKey</a>: <i>String</i>
    <a href="#awsapipath" title="AwsApiPath">AwsApiPath</a>: <i>String</i>
    <a href="#awsapistage" title="AwsApiStage">AwsApiStage</a>: <i>String</i>
    <a href="#awsdomain" title="AwsDomain">AwsDomain</a>: <i>String</i>
    <a href="#awsregion" title="AwsRegion">AwsRegion</a>: <i>String</i>
    <a href="#azureapikey" title="AzureApiKey">AzureApiKey</a>: <i>String</i>
    <a href="#azureapp" title="AzureApp">AzureApp</a>: <i>String</i>
    <a href="#azuredomain" title="AzureDomain">AzureDomain</a>: <i>String</i>
    <a href="#azurefunction" title="AzureFunction">AzureFunction</a>: <i>String</i>
    <a href="#azurefunctionauthorization" title="AzureFunctionAuthorization">AzureFunctionAuthorization</a>: <i>String</i>
    <a href="#delay" title="Delay">Delay</a>: <i>Double</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#emailbody" title="EmailBody">EmailBody</a>: <i>String</i>
    <a href="#emailfrom" title="EmailFrom">EmailFrom</a>: <i>String</i>
    <a href="#emailsubject" title="EmailSubject">EmailSubject</a>: <i>String</i>
    <a href="#gcpfunction" title="GcpFunction">GcpFunction</a>: <i>String</i>
    <a href="#gcpfunctiondomain" title="GcpFunctionDomain">GcpFunctionDomain</a>: <i>String</i>
    <a href="#gcpfunctionregion" title="GcpFunctionRegion">GcpFunctionRegion</a>: <i>String</i>
    <a href="#gcpproject" title="GcpProject">GcpProject</a>: <i>String</i>
    <a href="#httpbody" title="HttpBody">HttpBody</a>: <i>String</i>
    <a href="#message" title="Message">Message</a>: <i>String</i>
    <a href="#method" title="Method">Method</a>: <i>String</i>
    <a href="#minimuminterval" title="MinimumInterval">MinimumInterval</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#replacementmessage" title="ReplacementMessage">ReplacementMessage</a>: <i>String</i>
    <a href="#required" title="Required">Required</a>: <i>String</i>
    <a href="#script" title="Script">Script</a>: <i>String</i>
    <a href="#securitytag" title="SecurityTag">SecurityTag</a>: <i>String</i>
    <a href="#tlscertificate" title="TlsCertificate">TlsCertificate</a>: <i>String</i>
    <a href="#uri" title="Uri">Uri</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#emailto" title="EmailTo">EmailTo</a>: <i>
      - <a href="emailtodefinition.md">EmailToDefinition</a></i>
    <a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
    <a href="#sdnconnector" title="SdnConnector">SdnConnector</a>: <i>
      - <a href="sdnconnectordefinition.md">SdnConnectorDefinition</a></i>
</pre>

## Properties

#### Accprofile

Access profile for CLI script action to access FortiGate features.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionType

Action type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudAccessKeyId

AliCloud AccessKey ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudAccessKeySecret

AliCloud AccessKey secret.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudAccountId

AliCloud account ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudFunction

AliCloud function name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudFunctionAuthorization

AliCloud function authorization type. Valid values: `anonymous`, `function`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudFunctionDomain

AliCloud function domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudRegion

AliCloud region.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudService

AliCloud service name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudVersion

AliCloud version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsApiId

AWS API Gateway ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsApiKey

AWS API Gateway API key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsApiPath

AWS API Gateway path.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsApiStage

AWS API Gateway deployment stage name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsDomain

AWS domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsRegion

AWS region.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureApiKey

Azure function API key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureApp

Azure function application name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureDomain

Azure function domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureFunction

Azure function name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureFunctionAuthorization

Azure function authorization level. Valid values: `anonymous`, `function`, `admin`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Delay

Delay before execution (in seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailBody

Email body.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailFrom

Email sender name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailSubject

Email subject.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpFunction

Google Cloud function name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpFunctionDomain

Google Cloud function domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpFunctionRegion

Google Cloud function region.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpProject

Google Cloud Platform project name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpBody

Request body (if necessary). Should be serialized json string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

Message content.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

Request method (POST, PUT, GET, PATCH or DELETE). Valid values: `post`, `put`, `get`, `patch`, `delete`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumInterval

Limit execution to no more than once in this interval (in seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Protocol port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Request protocol. Valid values: `http`, `https`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacementMessage

Enable/disable replacement message. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Required

Required in action chain. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Script

CLI script.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityTag

NSX security tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsCertificate

Custom TLS certificate for API request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

Request API URI.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailTo

_Required_: No

_Type_: List of <a href="emailtodefinition.md">EmailToDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdnConnector

_Required_: No

_Type_: List of <a href="sdnconnectordefinition.md">SdnConnectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

