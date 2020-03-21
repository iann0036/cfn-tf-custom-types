# Terraform::AzureRM::MonitorActionGroup AzureFunctionReceiver

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#functionappresourceid" title="FunctionAppResourceId">FunctionAppResourceId</a>" : <i>String</i>,
    "<a href="#functionname" title="FunctionName">FunctionName</a>" : <i>String</i>,
    "<a href="#httptriggerurl" title="HttpTriggerUrl">HttpTriggerUrl</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#usecommonalertschema" title="UseCommonAlertSchema">UseCommonAlertSchema</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#functionappresourceid" title="FunctionAppResourceId">FunctionAppResourceId</a>: <i>String</i>
<a href="#functionname" title="FunctionName">FunctionName</a>: <i>String</i>
<a href="#httptriggerurl" title="HttpTriggerUrl">HttpTriggerUrl</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#usecommonalertschema" title="UseCommonAlertSchema">UseCommonAlertSchema</a>: <i>Boolean</i>
</pre>

## Properties

#### FunctionAppResourceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionName

The function name in the function app.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpTriggerUrl

The http trigger url where http request sent to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Azure Function receiver.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCommonAlertSchema

Enables or disables the common alert schema.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

