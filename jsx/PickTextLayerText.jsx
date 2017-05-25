/***
 * Pick Text Layer Text
 *
 * Author: Hidetsugu TAKAHASHI
 * Date: 2017-05-19
 *
 * = What's this?
 * psdファイルのテキストオブジェクトから、文字列を抽出するスクリプトです。
 *
 * = Reference
 * [Photoshop CC 自動化作戦](http://www.openspc2.org/book/PhotoshopCC/normal/layer/003/index.html)
 */

var CR = String.fromCharCode(13);

var save_name = File.saveDialog("保存するファイル名を指定してください。");

if (save_name) {
  file_object = new File(save_name);
  var write_flag = file_object.open("w");
  if (write_flag == true) {
    pickText(activeDocument);
    file_object.close();
  } else {
    alert("ファイルが開けませんでした。");
  }
}

/**
 * pickText
 *
 * ドキュメントのテキストレイヤーから文字を抽出し、ファイルに書き込みます。
 *
 * @param {layer} [document] - ドキュメントオブジェクト
 */
function pickText(layer) {

  var layer_len = layer.artLayers.length;
  for (var i=0; i<layer_len; i++) {
    if (layer.artLayers[i].kind === LayerKind.TEXT) {
      file_object.write(layer.artLayers[i].textItem.contents);// 文字列を追加
      file_object.write(CR); // レイヤー区別のために空行を追加
    }
  }

  // レイヤーセットの場合、再帰呼び出し。
  var layer_set = layer.layerSets.length;
  for (var i=0; i<layer_set; i++) {
    pickText(layer.layerSets[i]);
  }
}
