# TF::AWS::AppmeshVirtualNode ListenerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connectionpool" title="ConnectionPool">ConnectionPool</a>" : <i>[ <a href="connectionpooldefinition.md">ConnectionPoolDefinition</a>, ... ]</i>,
    "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ <a href="healthcheckdefinition.md">HealthCheckDefinition</a>, ... ]</i>,
    "<a href="#outlierdetection" title="OutlierDetection">OutlierDetection</a>" : <i>[ <a href="outlierdetectiondefinition.md">OutlierDetectionDefinition</a>, ... ]</i>,
    "<a href="#portmapping" title="PortMapping">PortMapping</a>" : <i>[ <a href="portmappingdefinition.md">PortMappingDefinition</a>, ... ]</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>[ <a href="timeoutdefinition.md">TimeoutDefinition</a>, ... ]</i>,
    "<a href="#tls" title="Tls">Tls</a>" : <i>[ <a href="tlsdefinition.md">TlsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#connectionpool" title="ConnectionPool">ConnectionPool</a>: <i>
      - <a href="connectionpooldefinition.md">ConnectionPoolDefinition</a></i>
<a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>
      - <a href="healthcheckdefinition.md">HealthCheckDefinition</a></i>
<a href="#outlierdetection" title="OutlierDetection">OutlierDetection</a>: <i>
      - <a href="outlierdetectiondefinition.md">OutlierDetectionDefinition</a></i>
<a href="#portmapping" title="PortMapping">PortMapping</a>: <i>
      - <a href="portmappingdefinition.md">PortMappingDefinition</a></i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>
      - <a href="timeoutdefinition.md">TimeoutDefinition</a></i>
<a href="#tls" title="Tls">Tls</a>: <i>
      - <a href="tlsdefinition.md">TlsDefinition</a></i>
</pre>

## Properties

#### ConnectionPool

_Required_: No

_Type_: List of <a href="connectionpooldefinition.md">ConnectionPoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

_Required_: No

_Type_: List of <a href="healthcheckdefinition.md">HealthCheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutlierDetection

_Required_: No

_Type_: List of <a href="outlierdetectiondefinition.md">OutlierDetectionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortMapping

_Required_: No

_Type_: List of <a href="portmappingdefinition.md">PortMappingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: List of <a href="timeoutdefinition.md">TimeoutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tls

_Required_: No

_Type_: List of <a href="tlsdefinition.md">TlsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

