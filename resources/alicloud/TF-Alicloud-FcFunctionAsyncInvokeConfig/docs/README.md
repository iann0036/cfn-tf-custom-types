# TF::Alicloud::FcFunctionAsyncInvokeConfig

CloudFormation equivalent of alicloud_fc_function_async_invoke_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::FcFunctionAsyncInvokeConfig",
    "Properties" : {
        "<a href="#functionname" title="FunctionName">FunctionName</a>" : <i>String</i>,
        "<a href="#maximumeventageinseconds" title="MaximumEventAgeInSeconds">MaximumEventAgeInSeconds</a>" : <i>Double</i>,
        "<a href="#maximumretryattempts" title="MaximumRetryAttempts">MaximumRetryAttempts</a>" : <i>Double</i>,
        "<a href="#qualifier" title="Qualifier">Qualifier</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
        "<a href="#destinationconfig" title="DestinationConfig">DestinationConfig</a>" : <i>[ <a href="destinationconfigdefinition.md">DestinationConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::FcFunctionAsyncInvokeConfig
Properties:
    <a href="#functionname" title="FunctionName">FunctionName</a>: <i>String</i>
    <a href="#maximumeventageinseconds" title="MaximumEventAgeInSeconds">MaximumEventAgeInSeconds</a>: <i>Double</i>
    <a href="#maximumretryattempts" title="MaximumRetryAttempts">MaximumRetryAttempts</a>: <i>Double</i>
    <a href="#qualifier" title="Qualifier">Qualifier</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
    <a href="#destinationconfig" title="DestinationConfig">DestinationConfig</a>: <i>
      - <a href="destinationconfigdefinition.md">DestinationConfigDefinition</a></i>
</pre>

## Properties

#### FunctionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumEventAgeInSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumRetryAttempts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Qualifier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationConfig

_Required_: No

_Type_: List of <a href="destinationconfigdefinition.md">DestinationConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedTime

Returns the <code>CreatedTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModifiedTime

Returns the <code>LastModifiedTime</code> value.

