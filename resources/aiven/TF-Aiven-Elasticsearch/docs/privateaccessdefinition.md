# TF::Aiven::Elasticsearch PrivateAccessDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#elasticsearch" title="Elasticsearch">Elasticsearch</a>" : <i>[ <a href="elasticsearchdefinition.md">ElasticsearchDefinition</a>, ... ]</i>,
    "<a href="#kibana" title="Kibana">Kibana</a>" : <i>[ <a href="kibanadefinition.md">KibanaDefinition</a>, ... ]</i>,
    "<a href="#prometheus" title="Prometheus">Prometheus</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#elasticsearch" title="Elasticsearch">Elasticsearch</a>: <i>
      - <a href="elasticsearchdefinition.md">ElasticsearchDefinition</a></i>
<a href="#kibana" title="Kibana">Kibana</a>: <i>
      - <a href="kibanadefinition.md">KibanaDefinition</a></i>
<a href="#prometheus" title="Prometheus">Prometheus</a>: <i>String</i>
</pre>

## Properties

#### Elasticsearch

_Required_: No

_Type_: List of <a href="elasticsearchdefinition.md">ElasticsearchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kibana

_Required_: No

_Type_: List of <a href="kibanadefinition.md">KibanaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prometheus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

