# TF::Splunk::GlobalHttpEventCollector

Update Global HTTP Event Collector input configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Splunk::GlobalHttpEventCollector",
    "Properties" : {
        "<a href="#dedicatediothreads" title="DedicatedIoThreads">DedicatedIoThreads</a>" : <i>Double</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#enablessl" title="EnableSsl">EnableSsl</a>" : <i>Boolean</i>,
        "<a href="#maxsockets" title="MaxSockets">MaxSockets</a>" : <i>Double</i>,
        "<a href="#maxthreads" title="MaxThreads">MaxThreads</a>" : <i>Double</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#usedeploymentserver" title="UseDeploymentServer">UseDeploymentServer</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Splunk::GlobalHttpEventCollector
Properties:
    <a href="#dedicatediothreads" title="DedicatedIoThreads">DedicatedIoThreads</a>: <i>Double</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#enablessl" title="EnableSsl">EnableSsl</a>: <i>Boolean</i>
    <a href="#maxsockets" title="MaxSockets">MaxSockets</a>: <i>Double</i>
    <a href="#maxthreads" title="MaxThreads">MaxThreads</a>: <i>Double</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#usedeploymentserver" title="UseDeploymentServer">UseDeploymentServer</a>: <i>Double</i>
</pre>

## Properties

#### DedicatedIoThreads

Number of threads used by HTTP Input server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

Input disabled indicator.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSsl

Enable SSL protocol for HTTP data input. `true` = SSL enabled, `false` = SSL disabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSockets

Maximum number of simultaneous HTTP connections accepted. Adjusting this value may cause server performance issues and is not generally recommended. Possible values for this setting vary by OS.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxThreads

Maximum number of threads that can be used by active HTTP transactions. Adjusting this value may cause server performance issues and is not generally recommended. Possible values for this setting vary by OS.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

HTTP data input IP port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDeploymentServer

Indicates whether the event collector input writes its configuration to a deployment server repository. When this setting is set to 1 (enabled), the input writes its configuration to the directory specified as repositoryLocation in serverclass.conf.
Copy the full contents of the splunk_httpinput app directory to this directory for the configuration to work. When enabled, only the tokens defined in the splunk_httpinput app in this repository are viewable and editable on the API and the Data Inputs page in Splunk Web. When disabled, the input writes its configuration to $SPLUNK_HOME/etc/apps by default. Defaults to 0 (disabled).

_Required_: No

_Type_: Double

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

